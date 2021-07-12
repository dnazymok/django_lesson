from django.shortcuts import render, redirect
from .models import Post
from django import forms


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
        form = PostForm(request.POST)
        if form.is_valid():
            Post(title=form.cleaned_data["title"], content=form.cleaned_data["content"]).save()
            return redirect("/posts")
        return render(request, "posts/add.html", context={"form": form})

class PostForm(forms.Form):
    title = forms.CharField(min_length=5)
    content = forms.CharField(max_length=100)
