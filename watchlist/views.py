from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import WatchList, StreamPlatform
from .serializers import WatchListSerializer, StreamPlatformSerializer


class StreamPlatformAV(APIView):

    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(
            platform, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class WatchListAPIView(APIView):

    def get(self, request):
        watchlist = WatchList.objects.all()
        watchlist_serializer = WatchListSerializer(watchlist, many=True)
        return Response(watchlist_serializer.data)
    

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
