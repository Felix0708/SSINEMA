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

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_all(request, movie_title):
    movies = Movie.objects.filter(title__icontains=movie_title)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


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
        rating = int(request.data['rank'])

        # 리뷰 저장
        if not Review.objects.filter(movie=movie, user=request.user).exists():
            serializer = ReviewSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(movie=movie, user=request.user)
        else:
            return Response('이미 데이터 리뷰가 존재합니다.')

        # like_users 저장
        if rating >= 7:
            # 아래 조건은 필요 없을 것 같다. 리뷰를 중복으로 작성할 수 없기 때문
            if not movie.like_users.filter(pk=request.user.pk).exists():
                movie.like_users.add(request.user)
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
        review.save()
        serializer = ReviewSerializer(review)

        return Response(serializer.data)

    def delete_review():
        if request.user.pk == review.user.pk:
            if review.movie.pk == movie.pk:
                # Movie 자체를 삭제하는 것이 아니기 때문에 추가적인 like_users 제거 작업이 필요하다
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