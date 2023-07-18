from rest_framework.routers import DefaultRouter
from api import views
app_name = 'api'
router = DefaultRouter()
router.register(r"movie", views.MovieViewSet, basename='movie'),
router.register(r"user", views.UserViewSet, basename='user'),
router.register(r"profile", views.User_ProfileViewSet, basename='profile'),
router.register(r"comment", views.CommentViewSet, basename='comment'),

urlpatterns = []+router.urls
