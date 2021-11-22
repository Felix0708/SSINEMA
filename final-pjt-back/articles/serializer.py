from django.contrib.auth import get_user_model
from rest_framework import serializers
from accounts.serializers import UserDetailSerializer
from .models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    like_users = UserDetailSerializer(read_only=True,many=True)
    like_users_count = serializers.IntegerField(source='like_users.count', read_only=True)
    comment_set = CommentSerializer(read_only=True,many=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = "__all__"
        # API로 GET만 하고 POST나 PUT은 하지 않을 필드
        read_only_fields = ('user', 'view_count')

class ArticleListSerializer(serializers.ModelSerializer):
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    like_users_count = serializers.IntegerField(source='like_users.count', read_only=True)

    class Meta : 
        model = Article
        exclude =('content', 'like_users',)
        read_only_fields = ('user','view_count')



class ArticleCommentSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    class Meta : 
        model = Article
        fields = ('user', 'title')


class CommentSerializer(serializers.ModelSerializer):
    article = ArticleCommentSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"