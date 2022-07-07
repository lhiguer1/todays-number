from rest_framework import generics
from rest_framework import permissions
from db.models import Number
from db.serializers import NumberSerializer

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
