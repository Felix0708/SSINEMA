from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('login/', obtain_jwt_token),
    path('<str:username>/', views.profile, name='profile'),
    path('follow/<str:username>/', views.follow, name='follow'),

    # path('api-token-auth/', obtain_jwt_token),    
]