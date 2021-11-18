from typing import ContextManager
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .models import Movie, Review

from .serializers import MovieSerializer, ReviewSerializer, ReviewDetailSerializer

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def movielist(request):
    # movies = Movie.objects.all()
    latest_movies = Movie.objects.order_by('-release_data')[:50]
    highrate_movies = Movie.objects.order_by('-vote_average')[:50]
    mostpop_movies = Movie.objects.order_by('-popularity')[:50]


    latest_serializer = MovieSerializer(latest_movies,many=True)
    highrate_serializer = MovieSerializer(highrate_movies,many=True)
    mostpop_serializer = MovieSerializer(mostpop_movies,many=True)

    context = {
        "latest_movies": latest_serializer.data,
        "highrate_movies": highrate_serializer.data,
        "mostpop_serializer": mostpop_serializer.data
    }

    return Response(context)

@api_view(['GET'])
@permission_classes([AllowAny])
def moviedetail(request,movie_id):
    movie = get_object_or_404(Movie,movie_id=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def reviews_create(request, movie_id):
    movie = get_object_or_404(Movie,movie_id=movie_id)
    if request.method == 'GET':
        User = get_user_model()
        reviews = movie.review_set.all()
        infos = []
        for review in reviews:
            rinfo = ReviewSerializer(review).data
            userid = rinfo['user']
            user = get_object_or_404(User,pk=userid)
            username = user.username
            tp = rinfo
            tp['username'] = username
            infos.append(tp)
        return Response(infos)

    else:
        user = request.user
        # userid = request.data['user']
        # User = get_user_model()
        # Users = User.objects.all()
        # user = get_object_or_404(User,pk=userid)
        rating = int(request.data['rank'])
        serializer = ReviewSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie = movie, user = request.user)
            if rating >= 4:
                if not movie.like_users.filter(pk=user.pk).exists():
                    movie.like_users.add(user)
            # print(movie.like_users)
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['DELETE'])
def review_delete(request, review_pk):
    review = get_object_or_404(Review,pk=review_pk)
    review.delete()
    return Response({'id': review_pk}, status = status.HTTP_204_NO_CONTENT)

# @api_view(['GET'])
# @permission_classes([AllowAny])
# def bestFive(request):
#     movies = Movie.objects.all().order_by('-vote_average')[:20]
#     serializer = MovieSerializer(movies, many=True)
#     return Response(serializer.data)

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