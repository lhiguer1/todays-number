#!/usr/bin/sh
#
# Download subtitles for each video in vtt format
set -exu

PLAYLIST="https://youtube.com/playlist?list=PLTPQcjlcvvXFtR0R91Gh5j9Xi8cq0oN3Y"
SAVE_PATH="auto_gen_subs"
ARCHIVE_FILE="archive.log"

yt-dlp \
    "${PLAYLIST}" \
    --skip-download \
    --write-auto-subs \
    --sub-format vtt \
    --sleep-requests 2 \
    --sleep-subtitles 2 \
    --output "${SAVE_PATH}/%(upload_date>%Y-%m-%d)s.%(ext)s"
