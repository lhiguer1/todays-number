from django.core.management.base import BaseCommand, CommandError, CommandParser
from requests import Response, post
from urllib.parse import urlparse, ParseResult


class Command(BaseCommand):
    help = 'Get user auth token.'
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('username')
        parser.add_argument('password')
        parser.add_argument('endpoint', type=urlparse)

    def handle(self, *args, **options):
        endpoint:ParseResult = options['endpoint']
        endpoint = endpoint._replace(path='/auth/')


        response:Response = post(endpoint.geturl(), json={
            'username': options['username'],
            'password': options['password'],
        })

        if response.ok:
            self.stdout.write(self.style.SUCCESS(response.json()))
        else:
            self.stdout.write(self.style.ERROR(f'{response.status_code}: {response.text}'))
