import django_filters.rest_framework as filters
from .models import Number, LynchVideoInfo

class NumberFilterSet(filters.FilterSet):
    date = filters.DateFilter(field_name='date', lookup_expr='exact')
    date_after  = filters.DateFilter(field_name='date', lookup_expr='gte')
    date_before = filters.DateFilter(field_name='date', lookup_expr='lte')
    date_range  = filters.DateRangeFilter(field_name='date')

    class meta:
        model = Number
        fields = ['date', 'date_after', 'date_before', 'date_rage']

class LynchVideoInfoFilterSet(filters.FilterSet):
    publishedAt     = filters.DateFilter(field_name='publishedAt', lookup_expr='exact')
    publishedAfter  = filters.DateFilter(field_name='publishedAt', lookup_expr='gte')
    publishedBefore = filters.DateFilter(field_name='publishedAt', lookup_expr='lte')
    publishedRange  = filters.DateRangeFilter(field_name='publishedAt')

    class meta:
        model = LynchVideoInfo
        fields = [
            'publishedAt',
            'publishedAfter',
            'publishedBefore',
            'publishedRange',
        ]
