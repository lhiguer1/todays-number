from rest_framework import authentication, permissions


class BaseAuthenticationPermission:
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
