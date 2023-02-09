import datetime
import statistics
import collections
from django.db.models import QuerySet
from django.views.generic import TemplateView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import (
    authentication,
    permissions,
    response,
    views,
    viewsets,
)
from .filters import NumberFilterSet, LynchVideoInfoFilterSet
from .models import Number, LynchVideo, LynchVideoInfo
from .pagination import BasePageNumberPagination
from .serializers import (
    NumberSerializer,
    NumberUpdateSerializer,
    LynchVideoSerializer,
    LynchVideoInfoSerializer,
)

def _get_statistics(request=None):
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
        'frequency': dict(collections.Counter(sorted(sequence))),
        'last_picked': {i: last_picked(i) for i in range(1,11)},
    }
    return stats

class StatisticsView(views.APIView):
    def get(self, request, *args, **kwargs):
        return response.Response(_get_statistics(request=request))
        
class NumberViewset(viewsets.ModelViewSet):
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    queryset = Number.objects.all()

    pagination_class = BasePageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = NumberFilterSet

    def get_serializer_class(self):
        if self.action in ('update', 'partial_update'):
            return NumberUpdateSerializer
        else:
            return NumberSerializer

class HomeView(TemplateView):
    template_name = 'lynchnumbers/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["statistics"] = _get_statistics(request=self.request)
        return context
    
class AboutView(TemplateView):
    template_name = 'lynchnumbers/about.html'

class DocumentationView(TemplateView):
    template_name = 'lynchnumbers/documentation.html'


class LynchVideoViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = LynchVideo.objects.all()
    serializer_class = LynchVideoSerializer
    pagination_class = BasePageNumberPagination

    def perform_create(self, serializer):
        """Create a corresponding LynchVideoInfo instance"""
        # currently not implemented, for now just perform save
        return super().perform_create(serializer)

class LynchVideoInfoViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = LynchVideoInfo.objects.all()
    serializer_class = LynchVideoInfoSerializer
    pagination_class = BasePageNumberPagination

    filter_backends = [DjangoFilterBackend]
    filterset_class = LynchVideoInfoFilterSet
