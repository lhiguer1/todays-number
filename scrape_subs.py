#!/usr/bin/env python3
#
# Download subtitles for each video in vtt format
from yt_dlp import YoutubeDL

PLAYLIST = "https://youtube.com/playlist?list=PLTPQcjlcvvXFtR0R91Gh5j9Xi8cq0oN3Y"
SAVE_PATH="auto_gen_subs"
PATH = f"{SAVE_PATH}/%(upload_date>%Y-%m-%d)s.%(ext)s"

ydl_opts = {
	'skip_download': True,
	'writeautomaticsub': True,
	'subtitlesformat': 'vtt',
	'sleep_request': 2,
	'sleep_subtitles': 2,
	'outtmpl': f"{SAVE_PATH}/%(upload_date>%Y-%m-%d)s.%(ext)s"
	}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([PLAYLIST])


