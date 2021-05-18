from rest_framework import serializers, viewsets
from rest_framework.generics import get_object_or_404

from .models import (Profile, UserAddress)
from .serializers import (ProfileSerializer, UserAddressSerializer)
from accounts.permissions import IsOwnerOrReadOnly


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile
    serializer_class = ProfileSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly]


class UserAddressViewSet(viewsets.ModelViewSet):
    queryset = UserAddress
    serializer_class = UserAddressSerializer
    permission_classes =  [IsOwnerOrReadOnly]