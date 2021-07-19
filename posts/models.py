from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    categories = models.ManyToManyField('Category', through='PostCategories')

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class PostCategories(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, default=None, related_name='post')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, default=None, related_name='category')
    is_main = models.BooleanField(default=False)
