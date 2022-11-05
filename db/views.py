import datetime

from django.db.models import Q, QuerySet
from django.shortcuts import get_object_or_404
from rest_framework import (
    authentication,
    exceptions,
    generics,
    mixins,
    permissions,
)

from .models import Number
from .serializers import NumberSerializer, NumberRetrieveUpdateDestroySerializer

class BaseNumberMixin:
    queryset = Number.objects.all()
    serializer_class = NumberSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class NumberListAPIView(BaseNumberMixin, generics.ListAPIView):
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

class NumberRetrieveUpdateDestroyAPIView(BaseNumberMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NumberRetrieveUpdateDestroySerializer

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