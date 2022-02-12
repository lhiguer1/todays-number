#!/usr/bin/sh
set -exu

# download current days number of the day auto subs, 
yt-dlp --quiet --write-auto-subs --skip-download --convert-subs srt https://www.youtube.com/watch?v=A5phQWdk_mw -o "%(upload_date>%Y-%m-%d)s.%(ext)s"
