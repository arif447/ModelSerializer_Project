from django.shortcuts import render
from order import models
from order import serializer
from rest_framework import viewsets
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.product.objects.all()
    serializer_class = serializer.productSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = models.payment.objects.all()
    serializer_class = serializer.PaymentSerializer

