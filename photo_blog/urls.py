from django.conf.urls import url
from . import views
from .views import (
Home, ViewPost, CreatePost,
UpdatePost,DeletePost, ViewProfile,
CreateComment,DeleteComment,
LikePostAPI, ViewLikes, ViewNotifications
)


urlpatterns = [
    url(r'^$', Home.as_view(), name='photo_blog-home'),
    url(r'^search/', views.search, name='search'),
    url(r'^post/<int:pk>/', ViewPost.as_view(), name='photo_blog-detail'),
    url(r'^post/new/', CreatePost.as_view(), name='photo_blog-create'),
    url(r'^post/<int:pk>/update', UpdatePost.as_view(), name='photo_blog-update'),
    url(r'^post/<int:pk>/delete/', DeletePost.as_view(), name='photo_blog-delete'),
    url(r'^user/<str:username>/', ViewProfile.as_view(), name='photo_blog-profile'),
    url(r'^post/<int:pk>/comment/', CreateComment.as_view(), name='photo_blog-comment'),
    url(r'^comment/<int:pk>/delete/', DeleteComment.as_view(), name='photo_blog-delete_comment'),
    url(r'^post/<int:pk>/like_api/', LikePostAPI.as_view(), name='photo_blog-post_like_api'),
    url(r'^post/<int:pk>/likes/', ViewLikes.as_view(), name='photo_blog-post_likes'),
    url(r'^notifications/', ViewNotifications.as_view(), name='photo_blog-notifications'),
]