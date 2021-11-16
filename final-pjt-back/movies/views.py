from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Genre, Movie, Review
from .serializers.genre import GenreAllSerializer, GenreDetailSerializer
from .serializers.movie import MovieAllSerializer, MovieDetailSerializer
from .serializers.review import ReviewAllSerializer, ReviewDetailSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def review_list_or_create(request):
    def review_list():
        reviews = get_list_or_404(Review)
        serializer = ReviewAllSerializer(reviews, many=True)
        return Response(serializer.data)

    def review_create():
        serializer = ReviewAllSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return review_list()
    elif request.method == 'POST':
        return review_create()


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_or_update_or_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk) 
    
    def review_detail():
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data)

    def review_update():
        serializer = ReviewDetailSerializer(instance=review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def review_delete():
        review.delete()
        data = {
            'delete': f'데이터 {review_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return review_detail()
    elif request.method == 'PUT':
        return review_update()
    elif request.method == 'DELETE':
        return review_delete()


@api_view(['GET', 'POST'])
def movie_list_or_create(request):
    movies = get_list_or_404(Movie)
    def movie_list():
        serializer = ReviewDetailSerializer(movies, many=True)
        return Response(serializer.data)

    def movie_create():
        serializer = MovieDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return movie_list()
    elif request.method == 'POST':
        return movie_create()

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_or_update_or_delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    def movie_detail():
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)
    

    def movie_update():
        serializer = ReviewDetailSerializer(movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def movie_delete():
        movie.delete()
        data = {
            'delete': f'데이터 {movie_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


    if request.method == 'GET':
        return movie_detail()
    if request.method == 'POST':
        return movie_update()
    if request.method == 'DELETE':
        return movie_delete()


@api_view(['GET', 'POST'])
def genre_list_or_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    def genre_list():
        genres = get_list_or_404(Genre)
        serializer = GenreAllSerializer(genres, many=True)
        return Response(serializer.data)

    def genre_create():
        serializer = GenreDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return genre_list()
    elif request.method == 'POST':
        return genre_create()


@api_view(['GET', 'PUT', 'DELETE'])
def genre_detail_or_update_or_delete(request, genre_pk, movie_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)


    def genre_detail():
        serializer = GenreDetailSerializer(genre)
        return Response(serializer.data)
    
    def genre_update():
        serializer = GenreDetailSerializer(genre, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def genre_delete():
        genre.delete()
        data = {
            'delete': f'데이터 {genre_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
    
    if request.method == 'GET':
        return genre_detail()
    if request.method == 'POST':
        return genre_update()
    if request.method == 'DELETE':
        return genre_delete()