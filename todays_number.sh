#!/usr/bin/sh
#
# download current days number of the day auto subs, 
set -exu

PLAYLIST="https://youtube.com/playlist?list=PLTPQcjlcvvXFtR0R91Gh5j9Xi8cq0oN3Y"
SAVE_PATH="auto_gen_subs"

yt-dlp \
    "${PLAYLIST}" \
    --skip-download \
    --write-auto-subs \
    --sub-format vtt \
    --output "${SAVE_PATH}/%(upload_date>%Y-%m-%d)s.%(ext)s" \
    --playlist-end 6
