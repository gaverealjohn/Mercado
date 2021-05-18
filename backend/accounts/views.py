from rest_framework import viewsets

from .models import (Profile, UserAddress, UserReview)
from .serializers import (ProfileSerializer, UserAddressSerializer, UserReviewSerializer)
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


class UserReviewViewSet(viewsets.ModelViewSet):
    queryset = UserReview
    serializer_class = UserReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]