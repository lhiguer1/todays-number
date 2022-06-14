import re
import json
from yt_dlp.utils import PostProcessingError
from yt_dlp.postprocessor import PostProcessor
from pathlib import Path
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

class SaveInfoPP(PostProcessor):
    """Save info to json file"""
    def run(self, info:dict):
        try:
            file = Path(info['filepath']).resolve()
            info_json = file.with_suffix('.json')
            info_json.write_text(json.dumps(info))
        except Exception as e:
            raise PostProcessingError(f'Unable to save infodict for `{file.name}`: {e}')

        self.to_screen(f'Information dict saved to `{file.name}`')
        return [], info

class UpdateDatabasePP(PostProcessor):
    def run(self, info:dict):
        # TODO: Actually process
        file = Path(info['filepath']).resolve()
        self.to_screen(f'`{file.name}` saved processed and db updated.')
        return [], info
