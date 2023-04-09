from django.urls import path
from .views import (
    WatchListAPIView, StreamPlatformAV,
    StreamPlatformDetailAV, WatchDetailAV
)

app_name = 'watchlist'

urlpatterns = [
    path('', WatchListAPIView.as_view(), name='watchlists'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='watchlist-detail'),
    path('streams', StreamPlatformAV.as_view(), name='stream-list'),
    path('streams/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream-detail'),
]