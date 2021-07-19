from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name="index"),
    path('add', views.AddPostView.as_view(), name="add"),
    path('<int:pk>', views.PostDetailView.as_view(), name="add")
]
