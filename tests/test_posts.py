import pytest

from posts.models import Post
from tags.models import Tag, TaggedItem


@pytest.fixture
def post():
        post = Post.objects.create(title="Title", content="Content", status=Post.STATUS_PUBLISHED)

        tag1 = Tag.objects.create(name="tag 1")
        tag2 = Tag.objects.create(name="tag 2")

        TaggedItem.objects.create(tag=tag1, content_object=post)
        TaggedItem.objects.create(tag=tag2, content_object=post)

        return post


@pytest.mark.django_db
def test_get_tags_list(post):
    post = Post.objects.get(title="Title")
    assert post.get_tags_list() == ['tag 2', 'tag 1']


@pytest.mark.django_db
def test_success(post, client):
    resp = client.get('/posts/')
    assert resp.status_code == 200

