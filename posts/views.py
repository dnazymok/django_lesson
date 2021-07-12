from django.shortcuts import render, redirect
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


def add(request):
    if request.method == "GET":
        return render(
            request,
            "posts/add.html",
        )
    elif request.method == "POST":
        post_title = request.POST["title"]
        post_content = request.POST["content"]
        Post(title=post_title, content=post_content).save()
        return redirect("/posts")
