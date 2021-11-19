from rest_framework import serializers
from .models import Movie, Review
from accounts.serializers import UserDetailSerializer

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    class Meta:
        model = Review
        exclude =('updated_at',)
        read_only_fields = ('movie', 'user')
        # ('id','content', 'rank','username')