from rest_framework import serializers
from .models import WatchList, StreamPlatform

class WatchListSerializer(serializers.ModelSerializer):
    platform = serializers.CharField(source='platform.name')

    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = "__all__"