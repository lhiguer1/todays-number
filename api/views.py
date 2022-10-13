from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from django.db.models import Q, QuerySet
from db.models import Number
from db.serializers import NumberSerializer

class PingView(APIView):
    """Used to verify API server is running"""
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request:Request, *args, **kwargs):
        return Response({'success': True})

class NumberListView(generics.ListAPIView):
    queryset = Number.objects.all()
    serializer_class = NumberSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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

class NumberCreateView(generics.CreateAPIView):
    queryset = Number.objects.all()
    serializer_class = NumberSerializer

class NumberUpdateView(generics.UpdateAPIView):
    queryset = Number.objects.all()
    serializer_class = NumberSerializer

class NumberDestroyView(generics.DestroyAPIView):
    queryset = Number.objects.all()
    serializer_class = NumberSerializer
