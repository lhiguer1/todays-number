from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class PingAPIView(APIView):
    """Used to verify API server is running"""
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request:Request, *args, **kwargs):
        return Response({'success': True})