from django.test import TestCase

from tags.models import Tag, TaggedItem
from posts.models import Post

from django.test import Client


class PostTestCase(TestCase):
    def setUp(self):
        post = Post.objects.create(title="Title", content="Content", status=Post.STATUS_PUBLISHED)

        tag1 = Tag.objects.create(name="tag 1")
        tag2 = Tag.objects.create(name="tag 2")

        TaggedItem.objects.create(tag=tag1, content_object=post)
        TaggedItem.objects.create(tag=tag2, content_object=post)

    def test_get_tags_list(self):
        post = Post.objects.get(title="Title")
        self.assertEqual(post.get_tags_list(), ['tag 2', 'tag 1'])

    def test_published(self):
        posts = Post.objects.published()
        self.assertEqual(len(posts), 1)
        Post.objects.create(title="title 2", content="content 2")
        self.assertEqual(len(Post.objects.published()), 1)


class PostListViewCase(TestCase):
    def setUp(self):
        post = Post.objects.create(title="Title", content="Content", status=Post.STATUS_PUBLISHED)

        tag1 = Tag.objects.create(name="tag 1")
        tag2 = Tag.objects.create(name="tag 2")

        TaggedItem.objects.create(tag=tag1, content_object=post)
        TaggedItem.objects.create(tag=tag2, content_object=post)

    def test_success(self):
        c = Client()
        resp = c.get('/posts/')
        self.assertEqual(resp.status_code, 200)

    def test_create_post_throw_csrf(self):
        c = Client(enforce_csrf_checks=True)
        resp = c.post("/posts/add", data={'title': 'title', "content": 'content'})
        self.assertEqual(resp.status_code, 403)
