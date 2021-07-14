from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    # category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, default=None, related_name='posts')
    categories = models.ManyToManyField('Category')

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
