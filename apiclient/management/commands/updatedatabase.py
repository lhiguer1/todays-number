import requests
import shelve
from datetime import date
from pathlib import Path, WindowsPath, PosixPath
from urllib.parse import urlparse, ParseResult
from django.core.management.base import BaseCommand, CommandError, CommandParser
from rest_framework import status
from ._transcript import get_transcript, get_number_from_transcript


class Command(BaseCommand):
    help = 'Update database with info from files found in path'
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('authtoken', help='Authorization token')
        parser.add_argument('endpoint', type=urlparse)
        parser.add_argument('filepath', help='Video save path', type=Path)


    def handle(self, *args, **options):
        authtoken:str = options['authtoken']
        endpoint:ParseResult = options['endpoint']._replace(path='/api/numbers/')
        filepath:WindowsPath|PosixPath = options['filepath']

        all_vids = list(filepath.glob('*.flac'))
        yturl = lambda id: f'https://youtu.be/{id}'

        try:
            response = requests.get(endpoint._replace(path='/ping').geturl())
            assert (response.ok) and (response.json().get('success') == True), 'Unable to ping server'
        except (Exception, AssertionError) as e:
            self.stdout.write(self.style.NOTICE(f'[!] Unable to reach api endpoint: {e}'))
            return
        
        # only process files that have not already been added
        response = requests.get(endpoint.geturl())
        count = response.json()['count']
        response = requests.get(endpoint.geturl(), params={'page_size': count})

        response_numbers = response.json()['results']

        dates_to_ignore = [number['date'] for number in response_numbers]
        vids = list(filter(lambda f: f.name.split('.')[0] not in dates_to_ignore, all_vids))

        with shelve.open(str(filepath / 'failed.shelve'), writeback=True) as failed_log:
            for v in vids:
                new_number = {
                    'date': None,
                    'number': None,
                    'transcript': None,
                    'url': None,
                }
                self.stdout.write(f'[*] Processing {v.name}')
                try:
                    diso, urlid, _ = v.name.split('.')
                    new_number['url'] = yturl(urlid)
                    new_number['date'] = date.fromisoformat(diso)
                except Exception as e:
                    # self.stdout.write(self.style.NOTICE(f'[--] Unable to parse `{v}` title: {e}.'))
                    pass

                new_number['transcript'] = get_transcript(v)
                new_number['number'] = get_number_from_transcript(new_number['transcript'])
                
                headers = {
                    'Authorization': 'Token {}'.format(authtoken)
                }

                response = requests.post(endpoint.geturl(), data=new_number, headers=headers)

                if response.status_code == status.HTTP_201_CREATED:
                    self.stdout.write(self.style.SUCCESS(f'[+] {new_number} added to database.'))
                else:
                    self.stdout.write(self.style.ERROR(f'[-] Failed to add {new_number} to database.'))
                    if new_number not in failed_log.setdefault('numbers', []):
                        failed_log['numbers'].append(new_number)
                        failed_log.sync()
            