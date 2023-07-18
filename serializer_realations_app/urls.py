from django.urls import path
from serializer_realations_app import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r"singer", views.SingerViewSet, basename='singer'),
router.register(r"song", views.SongViewSet, basename='song'),

urlpatterns = []+router.urls
