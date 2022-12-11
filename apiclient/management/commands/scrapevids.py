from django.core.management.base import BaseCommand, CommandParser
from pathlib import Path, WindowsPath, PosixPath
from urllib.parse import urlparse, ParseResult
from yt_dlp import (
    postprocessor,
    YoutubeDL,
)
from ._postprocessor import ChangeNamePP

class Command(BaseCommand):
    help = 'Scrape video from playlist.'
    def add_arguments(self, parser: CommandParser):
        parser.add_argument('playlist', help='Playlist URL', type=urlparse)
        parser.add_argument('filepath', help='Video save path', type=Path)

    def handle(self, *args, **options):
        playlist:ParseResult = options['playlist']
        filepath:WindowsPath|PosixPath = options['filepath']

        ydl_opts = {
            'ignoreerrors': True, # workaround for broken PostProcessor
            'sleep_interval': 3,
            'max_sleep_interval': 6,
            'format': 'bestaudio',
            'download_archive': filepath / 'archive.txt',
            'paths': {
                'home': filepath.as_posix()
            },
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.add_post_processor(postprocessor.FFmpegExtractAudioPP(preferredcodec='flac'))
            ydl.add_post_processor(ChangeNamePP())
            ydl.download([playlist.geturl()])

        self.stdout.write(self.style.SUCCESS(f'Files saved to {filepath}.'))
