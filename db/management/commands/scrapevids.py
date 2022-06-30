from django.core.management.base import BaseCommand
from yt_dlp import YoutubeDL
from yt_dlp.postprocessor import FFmpegExtractAudioPP
from ._postprocessors import ChangeNamePP
from ._common import DATA_PATH, PLAYLIST_URL

class Command(BaseCommand):
    help='Scrape playlist and save to `data` directory.'

    def handle(self, *args, **options):
        ydl_opts = {
            # 'ignoreerrors': True, # workaround for broken PostProcessor
            'sleep_interval': 3,
            'max_sleep_interval': 6,
            'format': 'bestaudio',
            'download_archive': DATA_PATH / 'archive.txt',
            'paths': {
                'home': DATA_PATH.as_posix()
            },
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.add_post_processor(FFmpegExtractAudioPP(preferredcodec='flac'))
            ydl.add_post_processor(ChangeNamePP())
            ydl.download([PLAYLIST_URL])

        self.stdout.write(self.style.SUCCESS(f'Files saved to {DATA_PATH}.'))