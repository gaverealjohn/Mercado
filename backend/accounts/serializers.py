from rest_framework import serializers
from django.conf import settings

from .models import (User, Profile, UserAddress, UserReview)
from store.models import (Product, ProductReview, Cart)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id',
            'user',
            'slug',
            'image',
            'dob',
            'gender',
            'bio'
        ]
        read_only_fields = ['user']
        depth = 1


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = [
            'address_line1', 
            'address_line2', 
            'city',
            'postal_code',
            'country'
        ]


class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReview
        fields = [
            'recipient',
            'rating',
            'title',
            'body',
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'phone_number',
            'first_name',
            'last_name',
            'email',
            'is_active'
        ]