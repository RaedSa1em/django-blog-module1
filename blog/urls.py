from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import CommentViewSet
from .views import UserViewSet
from .views import CategoryViewSet
from .views import PostViewSet, get_posts


from .views import generate , generate_post
from .views import summarize_post_view   


#router = DefaultRouter()
#router.register('posts', PostViewSet)
#router.register('users', UserViewSet)
#router.register('categories', CategoryViewSet)
#router.register('comments', CommentViewSet)


urlpatterns = [

    path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('categories/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category-list'),
    path('posts/', PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='post-list'),
    path('comments/',CommentViewSet.as_view({'get': 'list', 'post': 'create'}),name='comment-list',),
    path('posts/get_post/', get_posts, name='get_post'),
    path('posts/generate/', generate_post, name='generate_post'),
    path('posts/summarize/<int:post_id>/', summarize_post_view, name='summarize_post'),


]

#urlpatterns += router.urls
