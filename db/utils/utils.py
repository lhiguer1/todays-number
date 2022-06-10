#!/usr/bin/env python3
from pathlib import Path
from yt_dlp import YoutubeDL
from postprocessors import (
    AddTitleDateKeyPP,
    UpdateDatabasePP,
    ChangeNamePP,
    SaveInfoPP)

DATA_PATH = Path(__file__).resolve().parent.parent / 'data'
AUDIO_ONLY_PATH = DATA_PATH / 'audio_only/'
VIDS_PATH = DATA_PATH / 'vids/'

PLAYLIST = "https://youtube.com/playlist?list=PLTPQcjlcvvXFtR0R91Gh5j9Xi8cq0oN3Y"

def update_database():
    ydl_opts = {
        'ignoreerrors': True, # workaround for broken PostProcessor
        'sleep_interval': 3,
        'max_sleep_interval': 6,
        'format': 'bestaudio',
        'download_archive': AUDIO_ONLY_PATH / 'archive.txt',
        'paths': {
            'home': AUDIO_ONLY_PATH.as_posix()
            },
        }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.add_post_processor(AddTitleDateKeyPP())
        ydl.add_post_processor(ChangeNamePP())
        ydl.add_post_processor(UpdateDatabasePP())
        ydl.add_post_processor(SaveInfoPP())
        ydl.download([PLAYLIST])