from django.urls import path
from order import views
from rest_framework.routers import DefaultRouter
app_name = 'order'
router = DefaultRouter()
router.register(r"product", views.ProductViewSet, basename='product')
router.register(r'payment', views.PaymentViewSet, basename='payment')

urlpatterns = []+router.urls