from django.urls import path
from . import views

app_name = 'dummydata'

urlpatterns = [
    path('userdata/', views.create_user),
    path('articledata/', views.create_article),
    path('moviedata/', views.create_movies),
]