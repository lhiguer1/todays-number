import requests
import urllib.parse
import re
from datetime import date
from pathlib import Path
from django.core.management.base import BaseCommand, CommandParser
import speech_recognition as sr
import shelve

from rest_framework import status

from db.models import Number
from db.serializers import NumberSerializer
from ._common import DATA_PATH

class Command(BaseCommand):
    help='Find unprocessed videos and update database. Run `scrapevids` command first.'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('--baseurl',
            type=urllib.parse.urlparse,
            default='http://127.0.0.1:8000/',
            help='Location of endpoints.'
        )

        parser.add_argument('--authtoken',
            type=str,
            help='Authorization token',
            required=True
        )

    def get_number_from_transcript(cls, transcript):
        """Return number extracted from transcript. Return None if number is not found."""
        if not transcript:
            return None

        numbers = {
            '10': 10, 'ten': 10,
            '9': 9,   'nine': 9,
            '8': 8,   'eight': 8,
            '7': 7,   'seven': 7,
            '6': 6,   'six': 6,
            '5': 5,   'five': 5,
            '4': 4,   'four': 4,
            '3': 3,   'three': 3,
            '2': 2,   'two': 2,
            '1': 1,   'one': 1,
        }
        num_pattern = '|'.join(i for i in numbers)
        pattern = f'today\'?s number is.*(?P<todays_number>{num_pattern})'
        m = re.search(pattern, transcript)
        if m:
            return numbers[m.group('todays_number')]

    def get_transcript(cls, file:Path):
        try:
            r = sr.Recognizer()
            with sr.AudioFile(file.as_posix()) as source:
                audio = r.record(source)
                transcript = r.recognize_google(audio)
                return transcript
        except sr.UnknownValueError:
            pass
            # raise sr.UnknownValueError(f"Google Speech Recognition could not understand audio for {file}")
        except sr.RequestError as e:
            pass
            # raise sr.UnknownValueError(f"Could not request results from Google Speech Recognition service for {file}: {e}")

    def handle(self, *args, **options):
        api_endpoint: urllib.parse.ParseResult = options['baseurl']
        yturl = lambda id: f'https://youtu.be/{id}'
        all_vids = list(DATA_PATH.glob('*.flac'))

        try:
            response = requests.get(api_endpoint._replace(path='/api/ping').geturl())
            assert (response.status_code == 200) and (response.json().get('success') == True), 'Unable to ping server'
        except (Exception, AssertionError) as e:
            self.stdout.write(self.style.NOTICE(f'Unable to reach api endpoint: {e}'))
            return
        
        # only process files that have not already been added
        response = requests.get(api_endpoint._replace(path='/api/').geturl())
        response_numbers = response.json()['numbers']

        dates_to_ignore = [number['date'] for number in response_numbers]
        vids = list(filter(lambda f: f.name.split('.')[0] not in dates_to_ignore, all_vids))

        with shelve.open(str(DATA_PATH / 'failed.shelve'), writeback=True) as failed_log:
            for v in vids:
                new_number = Number()
                self.stdout.write(f'[*] Processing {v.name}')
                try:
                    diso, urlid, _ = v.name.split('.')
                    new_number.url = yturl(urlid)
                    new_number.date = date.fromisoformat(diso)
                except Exception as e:
                    pass
                    # self.stdout.write(self.style.NOTICE(f'[--] Unable to parse `{v}` title: {e}.'))

                new_number.transcript = self.get_transcript(v)
                new_number.number = self.get_number_from_transcript(new_number.transcript)
                
                serializer = NumberSerializer(new_number)
                headers = {
                    'Authorization': 'Token {}'.format(options['authtoken'])
                }

                response = requests.post(api_endpoint._replace(path='/api/add/').geturl(), data=serializer.data, headers=headers)

                if response.status_code == status.HTTP_201_CREATED:
                    self.stdout.write(self.style.SUCCESS(f'[+] {serializer.data} added to database.'))
                else:
                    self.stdout.write(self.style.ERROR(f'[-] Failed to add {serializer.data} to database.'))
                    if serializer.data not in failed_log.setdefault('numbers', []):
                        failed_log['numbers'].append(serializer.data)
                        failed_log.sync()
            