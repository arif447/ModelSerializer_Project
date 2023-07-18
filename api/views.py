from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api import serializer
from api import models
# Create your views here.

class MovieViewSet(ModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializer.MovieSerializer

class UserViewSet(ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializer.UserSerializer

class User_ProfileViewSet(ModelViewSet):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializer.UserProfileSerializer

class CommentViewSet(ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializer.CommentSerializer

