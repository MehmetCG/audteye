
from django.urls import path
from rest_framework.authtoken import views
from .views import (
    PostListCreateView,
    PostRetrieveUpdateDestroyView,
    CommentListCreateView
)

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path("post/", PostListCreateView.as_view(), name="post-list-create"),
    path("post/<pk>/", PostRetrieveUpdateDestroyView.as_view(), name="post-retrieve-update-destroy"),
    path("comment/", CommentListCreateView.as_view(), name="comment-list-create"),

]
