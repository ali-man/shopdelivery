from django.shortcuts import render
from rest_framework import viewsets

from appcatalogs.models import Category, Product
from appcatalogs.serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(show=True)
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(show=True)
    serializer_class = ProductSerializer
