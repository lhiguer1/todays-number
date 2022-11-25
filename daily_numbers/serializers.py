from daily_numbers.models import Number
from rest_framework import serializers

class NumberSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format='iso-8601', input_formats=['iso-8601'])
    number = serializers.IntegerField(min_value=1, max_value=10)
    url = serializers.URLField(allow_blank=False)
    transcript = serializers.CharField(allow_blank=False, trim_whitespace=True)

    class Meta:
        model = Number
        fields = (
            'date',
            'number',
            'url',
            'transcript',
        )

class NumberRetrieveUpdateDestroySerializer(NumberSerializer):
    date = serializers.DateField(read_only=True, format='iso-8601', input_formats=['iso-8601'])