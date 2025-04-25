from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserRegistrationSerializer


class UserViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
