from model_bakery import baker
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from posts.models import Post, Category


class APIQuizTest(APITestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse('category-list')
        baker.make(Category, _quantity=10)

    def _send_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.json()['results']

    def test_post_get_list(self):
        result = self._send_get()
        self.assertEqual(10, len(result))
