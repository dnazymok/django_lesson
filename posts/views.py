from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Post
from django import forms


class PostForm(forms.Form):
    title = forms.CharField(min_length=2)
    content = forms.CharField(max_length=100)

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 5:
            raise forms.ValidationError("Must be < 5")
        return title


class PostListView(ListView):
    model = Post
    template_name = "posts/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.published()


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_profile.html"
    context_object_name = "post"


class AddPostView(View):
    def get(self, request):
        form = PostForm()
        return render(
            request,
            "posts/add.html",
            {'form': form}
        )

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            Post(title=form.cleaned_data["title"], content=form.cleaned_data["content"]).save()
            return redirect("/posts")
        return render(request, "posts/add.html", context={"form": form})



