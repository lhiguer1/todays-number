from rest_framework import serializers
from .models import (
    Number,
    LynchVideo,
    LynchVideoInfo,
)

class NumberSerializer(serializers.HyperlinkedModelSerializer):
    url_field_name = 'detail'

    date = serializers.DateField(required=True)
    number = serializers.IntegerField(required=True, min_value=1, max_value=10)
    yt_video_id = serializers.RegexField(regex='^[\w\-]{11}$', label="YouTube Video ID", required=True, allow_blank=False, )
    yt_video_transcript = serializers.CharField(label="YouTube Video Transcript", required=True, allow_blank=False, trim_whitespace=True)

    class Meta:
        model = Number
        fields = (
            'date',
            'number',
            'detail',
            'yt_video_id',
            'yt_video_url',
            'yt_video_transcript',
            'yt_video',
        )

class NumberUpdateSerializer(NumberSerializer):
    """Same as NumberSerializer but 'date' (primary key) is uneditable."""
    class Meta(NumberSerializer.Meta):
        fields = (
            'number',
            'detail',
            'yt_video_id',
            'yt_video_transcript',
            'yt_video',
        )

class LynchVideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LynchVideo
        fields = (
            'url',
            'video',
        )


class LynchVideoInfoSerializer(serializers.HyperlinkedModelSerializer):
    video = LynchVideoSerializer(read_only=True)
    class Meta:
        model = LynchVideoInfo
        fields = (
            'url',
            'videoURL',
            'videoId',
            'publishedAt',
            'transcript',
            'number',
            'video',
        )
