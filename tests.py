from django.test import TestCase

from tags.models import Tag, TaggedItem
from posts.models import Category, Post


class PostTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="blablaCategory")
        post = Post.objects.create(title="Title", content="Content")

        tag1 = Tag.objects.create(name="tag 1")
        tag2 = Tag.objects.create(name="tag 2")

        TaggedItem.objects.create(tag=tag1, content_object=post)
        TaggedItem.objects.create(tag=tag2, content_object=post)

    def test_get_tags_list(self):
        post = Post.objects.get(title="Title")
        self.assertEqual(post.get_tags_list(), ['tag 2', 'tag 1'])
