from rest_framework import serializers
from .models import Movie,Review

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id','content', 'rank','user')
        read_only_fields = ('movie',)

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id','content', 'rank','username')
        read_only_fields = ('movie',)