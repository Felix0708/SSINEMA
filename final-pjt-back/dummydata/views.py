import requests
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from articles.models import Article
from movies.models import Movie

from faker import Faker
from django_seed import Seed
from decouple import config

import datetime

# Create your views here.

def create_user(request):
    fake = Faker()

    for f in range(10):
        get_user_model().objects.create(
            username=fake.name(), 
            password='abc',
            email=fake.email())
    return Response('testUser')

def create_article(request):
    fake = Faker()
    userList = get_user_model().objects.all()
    for f in range(2, 10):
        Article.objects.create(
            user = userList[f],
            title = fake.sentence(),
            content = fake.sentence())

    return Response('testArticle')

def create_movies(request):
    API_KEY = config('API_KEY')
    URL = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=ko-KR&page="
    for pageNum in range(1, 11):
        res = requests.get(URL + str(pageNum)).json()

        movie_list = res['results']
        for movie in movie_list:
            movie_id = movie["id"],
            title = movie["title"],
            vote_average = movie["vote_average"],
            vote_count = movie["vote_count"],   
            popularity = movie["popularity"],             
            release_date = datetime.datetime.strptime(movie["release_date"], "%Y-%m-%d").date()
            overview = movie["overview"],
            poster_path = movie["poster_path"],

            VIDEO_URL = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&append_to_response=videos"
            video_res = requests.get(VIDEO_URL).json()
            print('======================================================')
            print(video_res)
            print('======================================================')
            video_path = video_res["videos"]["results"][0]["key"]

            Movie.objects.create(
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
    print('======================================================')
    print('complete')
    print('======================================================')
    return Response('testArticle')


