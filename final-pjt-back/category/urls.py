from django.urls import path
from . import views

urlpatterns = [
    path('random/', views.random_movie, name='random_movie'),
    path('latest/', views.latest_movies, name='latest_movies'),
    path('toprate/', views.toprate_movies, name='toprate_movies'),    
    path('mostpop/', views.mostpop_movies, name='mostpop_movies'),
    path('foryou/', views.foruser_movies, name='foruser_movies'),
    path('weather/', views.weather_movies, name='weather_movies'),

]