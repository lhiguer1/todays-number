from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .mixins import BaseNumberMixin
from .pagination import NumberPageNumberPagination
from .filters import NumberFilterSet


class NumberViewset(BaseNumberMixin, viewsets.ModelViewSet):
    lookup_field = 'date'
    pagination_class = NumberPageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = NumberFilterSet
