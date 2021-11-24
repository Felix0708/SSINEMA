from django.urls import path, include
from . import views

urlpatterns = [
    path('category/', include('category.urls')),
    path('all/<str:movie_title>/', views.movie_all, name='movie_all'),
    path('<int:movie_id>/', views.moviedetail, name='moviedetail'),
    path('<int:movie_id>/review/', views.review_list_or_create, name='review_list_or_create'),    
    path('<int:movie_id>/review/<int:review_pk>/', views.review_detail_or_delete, name='review_detail_or_delete'),
    path('topRated/', views.topRated),

    # path('forUserMovieSave/', views.forUserMovieSave, name='forUserMovieSave'),
]