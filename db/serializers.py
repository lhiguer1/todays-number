from datetime import date
from db.models import Number
from rest_framework import serializers

class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = '__all__'

    def validate_date(self, d):
        if date(2020,1,1) <= d < date(2100,1,1):
            return d
        else:
            raise serializers.ValidationError('Valid dates are 2020-2100 exclusive.')

    def validate_number(self, number):
        if  1 <= number <= 10:
            return number
        else:
            raise serializers.ValidationError('Each ball has a number; numbers 1 through 10.')
