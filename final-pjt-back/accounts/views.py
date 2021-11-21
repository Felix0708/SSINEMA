from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserSerializer
from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model

from movies.models import Movie
from movies.serializers import MovieSerializer
from articles.models import Article, Comment
from articles.serializer import ArticleListSerializer, CommentSerializer


# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
    email = request.data.get('email')

    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()

        user.set_password(request.data.get('password'))
        user.save()
    # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않음
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def takename(request, user_pk):
    User = get_user_model()
    Users = User.objects.all()
    user = get_object_or_404(Users,pk=user_pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'username': person.username,
        'email': person.email,
        'followers': person.follwers.count(),
        'followings': person.followings.count()
    }
    return JsonResponse(context)



@api_view(['GET'])
@permission_classes([AllowAny])
def my_movie(request, username):
    like_movie = Movie.objects.filter(like_users=request.user.pk)
    serializer = MovieSerializer(like_movie, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def my_article(request, username):
    articles = Article.objects.filter(user=request.user)
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def my_comment(request, username):
    comments = Comment.objects.filter(user=request.user)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request, username):
    me = request.user
    you = get_object_or_404(get_user_model(), username=username)
    
    if me != you:

        # 내가 상대방(person)의 팔로워 목록에 있다면
        if you.followers.filter(pk=me.pk).exists():
        # 언팔로우
            you.followers.remove(me)
            followed = False
        else:
        # 팔로우
            you.followers.add(me)
            followed = True
        context = {
            'followed': followed,
            'followers_count': you.followers.count(),
            'followings_count': you.followings.count(),
        }
        return JsonResponse(context)