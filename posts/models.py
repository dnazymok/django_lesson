from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from tags.models import TaggedItem


class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status=Post.STATUS_PUBLISHED)


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()


class Post(models.Model):
    STATUS_DRAFT = 'D'
    STATUS_PUBLISHED = 'P'
    STATUS_REJECTED = 'R'
    STATUS = (
        (STATUS_DRAFT, 'Draft'),
        (STATUS_PUBLISHED, 'Published'),
        (STATUS_REJECTED, 'Rejected'),
    )

    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    status = models.CharField(choices=STATUS, default=STATUS_DRAFT, max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    categories = models.ManyToManyField('Category', through='PostCategories')
    tags = GenericRelation(TaggedItem)
    objects = PostManager()

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.title

    def get_tags_list(self):
        return [t.tag.name for t in self.tags.all().order_by('-tag__name')]


class Category(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class PostCategories(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, default=None, related_name='post')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, default=None, related_name='category')
    is_main = models.BooleanField(default=False)


class Comment(models.Model):
    text = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, default=None, related_name='comment_post')
    created_at = models.DateTimeField(auto_now_add=True)
