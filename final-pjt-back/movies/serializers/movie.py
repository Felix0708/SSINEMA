from django.db.models import fields
from rest_framework import serializers
from movies.serializers.review import ReviewDetailSerializer
from ..models import Review, Movie


class MovieAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieDetailSerializer(serializers.ModelSerializer):
    class ReviewDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('id', 'title')

    review = ReviewDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('title', 'overview', 'release_date', 'poster_path', 'review', 'actor',)

