import re
from pathlib import Path
from urllib import parse
from yt_dlp import YoutubeDL
from yt_dlp.postprocessor import FFmpegExtractAudioPP, PostProcessor
from yt_dlp.utils import PostProcessingError
from datetime import datetime


class ChangeNamePP(PostProcessor):
    """Change filename to {title_date}.{id}."""
    def get_title_date(cls, title):
        year_pattern  = r'(?P<year>\d{2})' # 2 digit year
        month_pattern = r'(?P<month>0\d|1[0-2]|\d)' # 1 or 2 digit month
        day_pattern   = r'(?P<day>3[01]|0\d|[12]\d|\d)' # 1 or 2 digit day

        try:
            match = re.search(f'{month_pattern}/{day_pattern}/{year_pattern}', title)
            dt = datetime.strptime(match.group(), '%m/%d/%y')
            d = dt.date()
        except Exception as e:
            raise PostProcessingError(f'Unable to add title_key to infodict: {e}')

        return d

    def run(self, info:dict):
        d = self.get_title_date(info['title'])
        try:
            id = info['id']
            title_date = d.isoformat()
            old_file = Path(info['filepath']).resolve()
            new_file = old_file.rename(old_file.with_stem(f'{title_date}.{id}'))

            info['filepath'] = str(new_file)
            info['title_date'] = title_date
        except Exception as e:
            raise PostProcessingError(f'Unable to change filename: {e}')

        self.to_screen(f'`{old_file.name}` renamed to `{new_file.name}`')
        return [], info

def scrapevids(playlist_url:str, save_path:Path):
    ydl_opts = {
        # 'ignoreerrors': True, # workaround for broken PostProcessor
        'sleep_interval': 3,
        'max_sleep_interval': 6,
        'format': 'bestaudio',
        'download_archive': save_path / 'archive.txt',
        'paths': {
            'home': save_path.as_posix()
        },
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.add_post_processor(FFmpegExtractAudioPP(preferredcodec='flac'))
        ydl.add_post_processor(ChangeNamePP())
        ydl.download([playlist_url])

    print(f'Files saved to {save_path}.')
