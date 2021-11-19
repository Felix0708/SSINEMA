from django.urls import path
from . import views

urlpatterns = [
    path('', views.movielist, name='movielist'),
    path('<int:movie_id>/', views.moviedetail, name='moviedetail'),
    path('<int:movie_id>/review/', views.review_list_or_create, name='review_list_or_create'),    
    path('<int:movie_id>/review/<int:review_pk>/', views.review_detail_or_delete, name='review_detail_or_delete'),
    path('topRated/', views.topRated),

    # path('forUserMovieSave/', views.forUserMovieSave, name='forUserMovieSave'),
]