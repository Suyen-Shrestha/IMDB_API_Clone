from django.urls import path
from .views import (
    WatchListAPIView, StreamPlatformAV,
    StreamPlatformDetailAV, WatchDetailAV,
    ReviewCreate, ReviewList, ReviewDetail
)

app_name = 'watchlist'

urlpatterns = [
    path('', WatchListAPIView.as_view(), name='watchlists'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='watchlist-detail'),
    path('streams', StreamPlatformAV.as_view(), name='stream-list'),
    path('streams/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
]