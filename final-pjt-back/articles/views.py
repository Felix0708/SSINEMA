from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Article, Comment
from .serializer import ArticleListSerializer, ArticleSerializer, CommentSerializer
from django.contrib.auth import get_user_model
from accounts.serializers import UserSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http.response import JsonResponse

from articles import serializer 

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def article_index(request):
    articles = get_list_or_404(Article.objects.order_by('-created_at'))
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_article(request):
    serializer = ArticleSerializer(data=request.data)            
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def article_detail_or_update_or_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    def article_detail():
        article.update_counter
        article.save()

        like_people = get_list_or_404(
            Article.objects.filter(pk=article_pk).values_list('like_users', flat=True))
        serializer = ArticleSerializer(article)

        context = {
            'serializer': serializer.data,
            'like_people': like_people,
        }
        return Response(context)

    def update_article():
        serializer = ArticleSerializer(instance=article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user = request.user,)
            return Response(serializer.data)
    
    def delete_article():
        if request.user.pk == article.user.pk:
            article.delete()
            context ={
                'delete':f'게시글 {article_pk}번 글이 삭제되었습니다.'
            }
            return Response(context, status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        return article_detail()
    elif request.method == 'PUT':
        return update_article()
    else:
        return delete_article()


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user

    if article.like_users.filter(pk=user.pk).exists():
        article.like_users.remove(user)
        liked = False
    else:
        article.like_users.add(user)
        liked = True

    like_people = get_list_or_404(
        Article.objects.filter(pk=article_pk).values_list('like_users', flat=True))

    context = {
        'liked': liked,
        'count': article.like_users.count(),
        'like_people': like_people,
    }
    return JsonResponse(context)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def comment_list_or_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    def comment_list():
        comments = get_list_or_404(Comment, article=article)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    def create_comment():
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=request.user)
            return Response(serializer.data, status= status.HTTP_201_CREATED)

    if request.method == 'GET':
        return comment_list()
    elif request.method == 'POST':
        return create_comment()

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_comment(request, comment_pk, article_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.user.pk == comment.user.pk:
        if comment.article.pk == article_pk:
            comment.delete()
            data = {
                'delete': f'데이터 {comment_pk}번 댓글이 삭제되었습니다'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_401_UNAUTHORIZED)