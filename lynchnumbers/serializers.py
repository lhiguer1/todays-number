from .models import Number
from rest_framework import serializers

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
        )

class NumberUpdateSerializer(NumberSerializer):
    """Same as NumberSerializer but 'date' (primary key) is uneditable."""
    class Meta(NumberSerializer.Meta):
        fields = (
            'number',
            'detail',
            'yt_video_id',
            'yt_video_transcript',
        )
