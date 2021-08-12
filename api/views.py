from rest_framework import viewsets, generics, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import BasePermission

from api.serializers import PostSerializer, CategorySerializer
from posts.models import Post, Category


class IsRegularUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_active


class PostViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsRegularUser]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
