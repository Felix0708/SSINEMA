from rest_framework import serializers
from ..models import Genre, Movie


class GenreAllSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name',)


class GenreDetailSerializer(serializers.ModelSerializer):

    class MovieDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title')

    title = serializers.CharField(min_length=1, max_length=100)
    movies = MovieDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = ('id', 'movies')
