from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from db.models import Number
from db.serializers import NumberSerializer

class PingView(APIView):
    """Used to verify API server is running"""
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        return Response({'success': True})

class NumberListView(generics.ListAPIView):
    queryset = Number.objects.all()
    serializer_class = NumberSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Return queryset filtered by specified date. Return all if none is provided.
        """
        filters = dict()

        for field in self.kwargs:
            key = f'date__{field}'
            filters[key] = self.kwargs[field]

        queryset = self.queryset
        queryset = queryset.filter(**filters)

        return queryset

class NumberCreateView(generics.CreateAPIView):
    queryset = Number.objects.all()
    serializer_class = NumberSerializer

class NumberUpdateView(generics.UpdateAPIView):
    queryset = Number.objects.all()
    serializer_class = NumberSerializer

class NumberDestroyView(generics.DestroyAPIView):
    queryset = Number.objects.all()
    serializer_class = NumberSerializer
