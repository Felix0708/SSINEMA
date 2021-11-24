from django.urls import path
from . import views

app_name = 'dummydata'

urlpatterns = [
    path('userdata/', views.create_user),
    path('articledata/', views.create_article),
    path('articlecommentdata/', views.create_article_comment),
    path('moviegenredata/', views.create_genres),
    path('moviedata/', views.create_movies),
    path('moviereviewdata/', views.create_movie_review),
    path('movieliekdata/', views.create_movie_like),
]