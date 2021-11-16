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
    
    # def create(self, validated_data):
    #     validated_data = validated_data['title']
    #     url = f'https://api.themoviedb.org/3/search/movie?api_key=adae75170a9e081a84916dbca45c6e43&query={validated_data}'
    #     data = requests.get(url).json()['results'][0]
    #     poster_path = f'https://image.tmdb.org/t/p/w500{data["poster_path"]}'
    #     overview = data['overview']
    #     release_data = data['release_date']

    #     movie = Movie()
    #     movie.poster_path = poster_path
    #     movie.overview = overview
    #     movie.title = validated_data
    #     movie.release_date = release_data
    #     movie.save()
    #     return movie

    class Meta:
        model = Movie
        fields = ('title', 'overview', 'release_date', 'poster_path', 'review', 'actors',)

