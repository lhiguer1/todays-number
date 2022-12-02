from rest_framework import authentication, permissions
from .models import Number
from .serializers import NumberSerializer


class BaseNumberMixin:
    queryset = Number.objects.all()
    serializer_class = NumberSerializer

class BaseAuthenticationPermission:
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
