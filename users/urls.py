from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from .views import FollowUser, ViewFollowers



urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    url(r'^edit_profile/', views.edit_profile, name='edit_profile'),
    url(r'^password_reset/',
          auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
          name='password_reset'),
    url(r'^password_reset/done/',
          auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
          name='password_reset_done'),
    url(r'^password_reset_confirm/<uidb64>/<token>/',
          auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
          name='password_reset_confirm'),
    url(r'^password_reset_complete/',
          auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
          name='password_reset_complete'),
    url(r'^user/<str:username>/follow/', FollowUser.as_view(), name='user_follow'),
    url(r'^user/<str:username>/followers/', ViewFollowers.as_view(), name='user_followers'),
]