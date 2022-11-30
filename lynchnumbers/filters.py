import django_filters.rest_framework as filters
from .models import Number

class NumberFilterSet(filters.FilterSet):
    date_after  = filters.DateFilter(field_name='date', lookup_expr='gte')
    date_before = filters.DateFilter(field_name='date', lookup_expr='lte')
    date_range  = filters.DateRangeFilter(field_name='date')

    class meta:
        model = Number
        fields = ['date', 'date_after', 'date_before', 'date_rage']
