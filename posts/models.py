from django.db import models


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
    objects = PostManager()

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
