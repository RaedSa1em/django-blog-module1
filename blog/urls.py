from django.urls import path

from rest_framework.routers import DefaultRouter

from blog.views.comment import CommentViewSet
from blog.views.user import UserViewSet
from blog.views.category import CategoryViewSet

from .views import PostViewSet, get_posts



urlpatterns = [
    path('posts/get_post/', get_posts, name='get_post'),
    path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('categories/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category-list'),
    path('posts/', PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='post-list'),
    path('comments/',CommentViewSet.as_view({'get': 'list', 'post': 'create'}),name='comment-list',)
]
