from .models import Number
from rest_framework import serializers

class NumberSerializer(serializers.HyperlinkedModelSerializer):
    url_field_name = 'detail'

    date = serializers.DateField(read_only=True, format='iso-8601', input_formats=['iso-8601'])
    number = serializers.IntegerField(min_value=1, max_value=10)
    url = serializers.URLField(allow_blank=False)
    transcript = serializers.CharField(allow_blank=False, trim_whitespace=True)

    class Meta:
        model = Number
        fields = (
            'date',
            'number',
            'detail',
            'url',
            'transcript',
        )
