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
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies,many=True)
    return Response(serializer.data)

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
        userid = request.data['user']
        User = get_user_model()
        Users = User.objects.all()
        user = get_object_or_404(Users,pk=userid)
        rating = int(request.data['rank'])
        serializer = ReviewSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie = movie, user = user)
            # if rating >= 7:
            #     if not movie.like_users.filter(pk=userid).exists():
            #         movie.like_users.add(user)
            # print(movie.like_users)
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['DELETE'])
def review_delete(request, review_pk):
    review = get_object_or_404(Review,pk=review_pk)
    review.delete()
    return Response({'id': review_pk}, status = status.HTTP_204_NO_CONTENT)