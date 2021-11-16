from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    comment_set = CommentSerializer(read_only=True,many=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = "__all__"

class ArticleListSerializer(serializers.ModelSerializer):
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    like_users_count = serializers.IntegerField(source='like_users.count', read_only=True)

    class Meta : 
        model = Article
        exclude =('like_users','view_count')