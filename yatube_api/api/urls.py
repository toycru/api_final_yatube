from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.views import PostViewSet, GroupViewSet, CommentViewSet

v1_router = SimpleRouter()
# api/v1/posts/ (GET, POST)
# api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE)
v1_router.register('posts', PostViewSet, basename='posts')
# api/v1/groups/ (GET): получаем список всех групп.
# api/v1/groups/{group_id}/ (GET): получаем информацию о группе по id.
v1_router.register('groups', GroupViewSet, basename='groups')
# api/v1/posts/{post_id}/comments/ (GET, POST)
# api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE)
v1_router.register('posts/(?P<post_id>\\d+)/comments', CommentViewSet,
                   basename='comments')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
