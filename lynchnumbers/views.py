import datetime
import statistics
import collections
from django.db.models import QuerySet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import (
    authentication,
    permissions,
    response,
    views,
    viewsets,
)
from .filters import NumberFilterSet
from .models import Number
from .pagination import NumberPageNumberPagination
from .serializers import NumberSerializer


class StatisticsView(views.APIView):
    def get(self, request, *args, **kwargs):
        qs:QuerySet = Number.objects.all()

        def last_picked(number) -> dict:
            d:datetime.date = qs.filter(number=number).latest('date')
            serializer = NumberSerializer(d, context={'request': request})

            return {
                'date': serializer.data['date'],
                'detail': serializer.data['detail']
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
        
class NumberViewset(viewsets.ModelViewSet):
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    queryset = Number.objects.all()
    serializer_class = NumberSerializer

    pagination_class = NumberPageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = NumberFilterSet