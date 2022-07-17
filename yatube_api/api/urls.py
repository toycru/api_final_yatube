from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet
from django.urls import include, path
from rest_framework.routers import SimpleRouter

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
# api/v1/follow/ (GET, POST)
v1_router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
