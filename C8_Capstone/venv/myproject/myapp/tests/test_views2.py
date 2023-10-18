from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ..models import MenuItem
from ..serializers import MenuItemSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_items = [
            MenuItem.objects.create(title="Item 1", price=10.99),
            MenuItem.objects.create(title="Item 2", price=15.99),
            MenuItem.objects.create(title="Item 3", price=8.99),
        ]

    def test_getall(self):
        response = self.client.get('/restaurant/menu-items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = MenuItemSerializer(self.menu_items, many=True).data
        self.assertJSONEqual(
            str(response.content, encoding='utf-8'), expected_data)
