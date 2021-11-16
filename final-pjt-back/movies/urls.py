from django.urls import path
from . import views

urlpatterns = [
    path('review/', views.review_list_or_create),
    path('review/<int:review_pk>/', views.review_detail_or_update_or_delete),

    path('movie/', views.movie_list_or_create),
    path('movie/<int:movie_pk>/', views.movie_detail_or_update_or_delete),

    path('movie/<int:movie_pk>/actor/', views.genre_list_or_create),
    path('movie/<int:movie_pk>/actor/<int:actor_pk>/', views.genre_detail_or_update_or_delete),
]