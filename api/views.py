from rest_framework import viewsets

from api.serializers import PostSerializer, CategorySerializer
from posts.models import Post, Category


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
