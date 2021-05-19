from rest_framework import serializers
from django.conf import settings

from .models import (User, Profile, UserAddress, UserReview)
from store.models import (Product, ProductReview, Cart)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['user']
        depth = 1


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = '__all__'
        read_only_fields = ['user']
        depth = 1


class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReview
        fields =  '__all__'
        read_only_fields = ['author', 'recipient']
        depth = 1

