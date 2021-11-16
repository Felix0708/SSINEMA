from rest_framework import serializers
from ..models import Review


class ReviewAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'title')


class ReviewDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('title',)
        read_only_fields = ('movie_id', 'user')