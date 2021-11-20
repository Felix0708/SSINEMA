from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # Article
    ## CRUD
    path('', views.article_index, name='article_index'),
    path('create/', views.create_article, name='create_article'),
    path('<int:article_pk>/', views.article_detail_or_update_or_delete, name='article_detail_or_update_or_delete'),
    
    ## Like
    path('<int:article_pk>/like/', views.like_article, name='like_article'),
    
    # Comment
    ## CD
    path('<int:article_pk>/comments/', views.comment_list_or_create, name='comment_list_or_create'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),
]
