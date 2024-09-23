from django.shortcuts import render
from rest_framework import viewsets

from .models import Article, category
from .serializers import ArticleSerializer, CategorySerializer


# Create your views here.

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = category.objects.all()
    serializer_class = CategorySerializer
