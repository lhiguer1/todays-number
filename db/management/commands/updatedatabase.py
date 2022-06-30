import re
from datetime import date
from pathlib import Path
from django.core.management.base import BaseCommand
import speech_recognition as sr

from ._common import DATA_PATH
from db.models import Number

class Command(BaseCommand):
    help='Find unprocessed videos and update database. Run `scrapevids` command first.'

    def get_number_from_transcript(cls, transcript):
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
        else:
            return None

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
        return ''
        

    def handle(self, *args, **options):
        files = DATA_PATH.glob('*.flac')
        succ_count = 0
        atmp_count = 0
        for f in files:
            self.stdout.write(f'[*] Processing {f.name}')
            try:
                diso, urlid, _ = f.name.split('.')
                d = date.fromisoformat(diso)
            except Exception as e:
                self.stdout.write(self.style.NOTICE(f'[--] Unable to process {f}: {e}.'))
                continue

            if Number.objects.filter(date=d, urlid=urlid).exists():
                self.stdout.write(f'[--] Number exists in database.')
                continue

            atmp_count += 1

            try:
                transcript = self.get_transcript(f)
            except Exception as e:
                self.stdout.write(self.style.NOTICE(f'[--] Unable to extract transcript from {f}: {e}.'))
                continue

            number = self.get_number_from_transcript(transcript)
            
            new_num = Number(date=d, number=number, urlid=urlid, transcript=transcript)
            new_num.save()
            succ_count += 1
            self.stdout.write(self.style.SUCCESS(f'[++] {d} added to database.'))

        self.stdout.write(self.style.SUCCESS(f'[++] {succ_count}/{atmp_count} processed.'))
        