from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('login/', obtain_jwt_token),
    path('<int:user_pk>/', views.takename),
    path('<str:username>/', views.profile_detail_or_update_or_delete, name='profile_detail_or_update_or_delete'),
    path('<int:user_pk>/myMovie/', views.my_movie, name='my_movie'),
    path('<int:user_pk>/myArticle/', views.my_article, name='my_article'),
    path('<int:user_pk>/myComment/', views.my_comment, name='my_comment'),
    path('follow/<str:username>/', views.follow, name='follow'),
    # path('api-token-auth/', obtain_jwt_token),
]