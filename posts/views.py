from django.shortcuts import render
from .models import Post


def index(request):
    context = {
        "posts": Post.objects.order_by("-created_on")
    }
    return render(
        request,
        "posts/index.html",
        context=context
    )
