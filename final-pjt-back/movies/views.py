from typing import ContextManager
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model

from .models import Genre, Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
from decouple import config

from django.db.models import Q
from collections import Counter

# Create your views here.
# @api_view(['GET'])
# @permission_classes([AllowAny])
# def movielist(request):
#     # DB 업데이트
#     TMDBHelper().create_movies()

#     # movies = Movie.objects.all()
#     latest_movies = Movie.objects.order_by('release_date').reverse()[:50]
#     toprate_movies = Movie.objects.order_by('vote_average').reverse()[:50]
#     mostpop_movies = Movie.objects.order_by('popularity').reverse()[:50]

#     like_movie = Movie.objects.filter(like_users=request.user.pk)

#     genre_list = []
#     for movie in like_movie:
#         genre_list += Movie.objects.filter(pk=movie.pk).values_list('genres', flat=True)
#     best_genre_pk = Counter(genre_list).most_common(1)[0][0]
#     second_genre_pk = Counter(genre_list).most_common(2)[0][0]

#     best_genre_movies = Movie.objects.filter(Q(genres=best_genre_pk) | Q(genres=second_genre_pk))

#     random_movie = Movie.objects.order_by('?')[0]

#     latest_serializer = MovieSerializer(latest_movies, many=True)
#     toprate_serializer = MovieSerializer(toprate_movies, many=True)
#     mostpop_serializer = MovieSerializer(mostpop_movies, many=True)
#     best_genre_serializer = MovieSerializer(best_genre_movies, many=True)
#     random_serializer = MovieSerializer(random_movie)

#     context = {
#         "latest_movies": latest_serializer.data,
#         "toprate_movies": toprate_serializer.data,
#         "mostpop_movies": mostpop_serializer.data,
#         "best_genre_movies": best_genre_serializer.data,
#         "random_movie": random_serializer.data,
#     }

#     return Response(context)

@api_view(['GET'])
@permission_classes([AllowAny])
def moviedetail(request,movie_id):
    movie = get_object_or_404(Movie, movie_id=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def review_list_or_create(request, movie_id):
    movie = get_object_or_404(Movie, movie_id=movie_id)

    def review_list():
        reviews = get_list_or_404(Review, movie=movie)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


    def create_review():
        user_id = int(request.data['user'])
        user = get_user_model().objects.get(pk=user_id)

        rating = int(request.data['rank'])

        # 리뷰 저장
        if not movie.like_users.filter(pk=user.pk).exists():
            serializer = ReviewSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(movie=movie, user=user)
        else:
            return Response('이미 데이터 리뷰가 존재합니다.')

        # like_users 저장
        if rating >= 7:
            if not movie.like_users.filter(pk=user_id).exists():
                movie.like_users.add(user)
        # print(movie.like_users)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return review_list()
    elif request.method == 'POST':
        return create_review()


@api_view(['GET', 'DELETE'])
@permission_classes([AllowAny])
def review_detail_or_delete(request, review_pk, movie_id):
    review = get_object_or_404(Review, pk=review_pk)
    movie = get_object_or_404(Movie, movie_id=movie_id)

    def review_detail():
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print(request)
        print(request.user)

        print(request.user.pk)
        print(request.user.id)
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

        review.save()
        serializer = ReviewSerializer(review)

        return Response(serializer.data)

    def delete_review():
        if request.user.pk == review.user.pk:
            if review.movie.pk == movie.pk:
                movie.like_users.remove(request.user)
                review.delete()

                context ={
                    'delete':f'게시글 {review_pk}번 후기가 삭제되었습니다.'
                }
                return Response(context, status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        return review_detail()
    elif request.method == 'DELETE':
        return delete_review()


@api_view(['GET'])
@permission_classes([AllowAny])
def topRated(request):
    movies = Movie.objects.all().order_by('-vote_average')[:20]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


#
# @api_view(['POST'])
# def forUserMovieSave(request):
#     # print(request.body)
#     chocie_movies = request.data['forusermovies']
#     for movie in chocie_movies:
#         print(movie['title'],movie['id'])
#         if not Movie.objects.filter(movie_id=movie['id']).exists():
#             print('new create')
            
#             Movie.objects.create(
#                 poster_path=movie['poster_path'],
#                 title=movie['title'],
#                 vote_average=movie['vote_average'],
#                 overview=movie['overview'],
#                 release_date=movie['release_date'],
#                 movie_id=movie['id'],
#                 )
#         else:
#             print('already have')
#             pass
#     return Response({'Movie': 'Movie'}, status= status.HTTP_202_ACCEPTED)