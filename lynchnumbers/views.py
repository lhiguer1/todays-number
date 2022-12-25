import datetime
import statistics
import collections
from django.db.models import QuerySet
from rest_framework import (
    response,
    reverse,
    views,
)
from .models import Number


class StatisticsView(views.APIView):
    def get(self, request, *args, **kwargs):
        qs:QuerySet = Number.objects.all()

        def last_picked(number) -> dict:
            d:datetime.date = qs.filter(number=number).latest('date').date
            return {
                'date': d,
                'detail': reverse.reverse('number-detail', kwargs={'date': d}, request=request)
            }

        sequence = qs.values_list('number', flat=True)
        stats = {
            'count': len(sequence),
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
        