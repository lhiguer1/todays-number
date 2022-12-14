import datetime
import statistics
import collections
from django.db.models import Q, QuerySet
from django.shortcuts import get_object_or_404
from rest_framework import (
    exceptions,
    generics,
    mixins,
    serializers,
    response,
    reverse,
)
from .mixins import BaseNumberMixin, BaseAuthenticationPermission


class NumberListAPIView(BaseNumberMixin, BaseAuthenticationPermission,generics.ListAPIView):
    def get_queryset(self):
        """
        Return queryset filtered by specified date. Return all if none is provided.
        """
        qs:QuerySet = super().get_queryset()
        lookup = Q()

        for field in self.kwargs:
            lookup &= Q(**{f'date__{field}': self.kwargs[field]})

        qs = qs.filter(lookup)

        return qs

class NumberListCreateAPIView(mixins.CreateModelMixin, NumberListAPIView):
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class NumberRetrieveUpdateDestroyAPIView(BaseNumberMixin, BaseAuthenticationPermission, generics.RetrieveUpdateDestroyAPIView):
    date = serializers.DateField(read_only=True, format='iso-8601', input_formats=['iso-8601'])

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        try:
            date = datetime.date.fromisoformat('{year:04}-{month:02}-{day:02}'.format_map(self.kwargs))
        except ValueError as e:
            raise exceptions.NotFound(e)

        obj = get_object_or_404(queryset, date=date)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj

class StatisticsView(BaseNumberMixin, BaseAuthenticationPermission, generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        qs:QuerySet = self.get_queryset()
        def last_picked(number) -> dict:
            d:datetime.date = qs.filter(number=number).latest('date').date
            return {
                'date': d,
                'singleton': reverse.reverse('number-detail', kwargs={'date': d}, request=request)
            }

        sequence = qs.values_list('number', flat=True)
        stats = {
            'count': qs.count(),
            'sequence': sequence,
            'sum': sum(sequence),
            'median': statistics.median(sequence),
            'mean': statistics.mean(sequence),
            'mode': statistics.mode(sequence),
            'variance': statistics.pvariance(sequence),
            'standard_deviation': statistics.pstdev(sequence),
            'frequency': collections.Counter(sorted(sequence)),
            'last_picked': {i: last_picked(i) for i in range(1,11)},
        }
        return response.Response(stats)
        