from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import (
InboxView, ThreadView, CreateDirectMessage, DeleteDirectMessage, ViewDirectMessage
)


urlpatterns = [
    url(r'^inbox/', InboxView.as_view(), name='direct_messages-inbox'),
    url(r'^thread/<str:username>/', ThreadView.as_view(), name='direct_messages-thread'),
    url(r'^new/', CreateDirectMessage.as_view(), name='direct_messages-new'),
    url(r'^<int:pk>/', ViewDirectMessage.as_view(), name='direct_messages-detail'),
    url(r'^<int:pk>/delete/', DeleteDirectMessage.as_view(), name='direct_messages-delete'),
    ]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
