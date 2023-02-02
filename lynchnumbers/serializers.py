from .models import Number
from rest_framework import serializers

class NumberSerializer(serializers.HyperlinkedModelSerializer):
    url_field_name = 'detail'

    date = serializers.DateField()
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

class NumberUpdateSerializer(NumberSerializer):
    """Same as NumberSerializer but 'date' (primary key) is uneditable."""
    class Meta(NumberSerializer.Meta):
        fields = (
            'number',
            'detail',
            'url',
            'transcript',
        )
