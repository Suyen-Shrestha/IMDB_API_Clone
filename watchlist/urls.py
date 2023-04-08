from django.urls import path
from .views import WatchListAPIView,StreamPlatformAV

app_name = 'watchlist'

urlpatterns = [
    path('', WatchListAPIView.as_view(), name='watchlists'),
    path('streams', StreamPlatformAV.as_view(), name='stream-list'),
]