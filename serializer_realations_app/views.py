from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from serializer_realations_app.models import Singer, Song
from serializer_realations_app.serializer import SingerSerializer, SongSerializer

# Create your views here.

class SingerViewSet(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

