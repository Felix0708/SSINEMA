import requests
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from articles.models import Article, Comment
from movies.models import Movie, Review, Genre

from faker import Faker
from django_seed import Seed
from decouple import config

import datetime

# Create your views here.

def create_user(request):
    fake = Faker('ko_KR')

    for f in range(10):
        get_user_model().objects.create(
            username=fake.name(), 
            password='abc',
            email=fake.email())
    return Response('testUser')


def create_article(request):
    fake = Faker('ko_KR')
    userList = get_user_model().objects.all()
    for f in range(2, 10):
        article = Article.objects.create(
            user = userList[f],
            title = fake.sentence(),
            content = fake.sentence())

        like_user = get_user_model().objects.get(pk=f+1)
        article.like_users.add(like_user)
    return Response('testArticle')


def create_article_comment(request):
    fake = Faker('ko_KR')
    userList = get_user_model().objects.all()
    articleList = Article.objects.all()

    for f in range(2, 10):
        Comment.objects.create(
            user = userList[f],
            article = articleList[f],
            content = fake.sentence())

    return Response('testArticleComment')


def create_genres(request):
    API_KEY = config('API_KEY')
    URL = f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=ko-KR"
    res = requests.get(URL).json()
    genre_list = res['genres']

    for genre in genre_list:
        Genre.objects.create(
            genre_id = genre['id'],
            name = genre['name']
        )
        # genre_id = genre['id']
        # name = genre['name']
    return Response('testGenre')


def create_movies(request):
    for old in Movie.objects.all() :
        old.delete()

    API_KEY = config('API_KEY')
    URL = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=ko-KR&page="
    # for pageNum in range(1, 10):
    for pageNum in range(1, 2):
        res = requests.get(URL + str(pageNum)).json()

        movie_list = res['results']
        for movie in movie_list:
            movie_id = movie['id']
            title = movie['title']
            vote_average = movie['vote_average']
            vote_count = movie['vote_count']
            popularity = movie['popularity']      
            release_date = datetime.datetime.strptime(movie["release_date"], "%Y-%m-%d").date()
            overview = movie["overview"]
            poster_path = movie["poster_path"]
            genre_ids_list = movie["genre_ids"]

            VIDEO_URL = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&append_to_response=videos"
            video_res = requests.get(VIDEO_URL).json()
            video_result = video_res["videos"]["results"]
            video_path = ''
            if video_result:
                video_path = video_result[0]['key']

            movie = Movie.objects.create(
                movie_id = movie_id,
                title = title,
                vote_average = vote_average,
                vote_count = vote_count,
                popularity = popularity,
                release_date = release_date,
                overview = overview,
                poster_path = poster_path,
                video_path = video_path
            )

            for genre in genre_ids_list:
                genre_object = Genre.objects.get(genre_id=genre)
                movie.genres.add(genre_object)


    print('======================================================')
    print('complete')
    print('======================================================')
    return Response('testMovie')


def create_movie_review(request):
    for old in Review.objects.all() :
        old.delete()

    fake = Faker('ko_KR')
    userList = get_user_model().objects.all()
    movieList = Movie.objects.all()

    for f in range(2, 10):
        Review.objects.create(
            user = userList[f],
            movie = movieList[f],
            content = fake.sentence(),
            rank = 5)

    print('======================================================')
    print('complete')
    print('======================================================')
    return Response('testMovieReview')


def create_movie_like(request):
    like_movie_list = Review.objects.filter(rank__gte=4).values_list('movie_id', 'user_id')
    for like_movie in like_movie_list:
        movie_object = Movie.objects.get(pk=like_movie[0])
        user_object = get_user_model().objects.get(pk=like_movie[1])
        movie_object.like_users.add(user_object)


