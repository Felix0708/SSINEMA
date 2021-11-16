from rest_framework import serializers
from ..models import Review
from accounts.serializers import UserSerializer


class ReviewAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'title')


class ReviewDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('title', 'user')
        read_only_fields = ('movie_id', 'user')