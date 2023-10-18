from django.test import TestCase
from myapp.models import MenuItem
from myapp.views import MenuItemsView
from django.core import serializers
from rest_framework.test import APIRequestFactory
import json


class MenuViewTest(TestCase):
    def setUp(self):
        # Create sample menu items for testing
        self.menu1 = MenuItem.objects.create(title="Dish 1", price=10.00)
        self.menu2 = MenuItem.objects.create(title="Dish 2", price=15.00)
        self.menu3 = MenuItem.objects.create(title="Dish 3", price=12.00)

    def test_get_all_menu_items(self):
        # Create a request for the MenuItemsView
        factory = APIRequestFactory()
        request = factory.get('/myapp/menu-items/')
        response = MenuItemsView.as_view()(request)

        # Render the response to access the content
        response.render()

        # Serialize the menu items and compare with the response content

        serialized_data = serializers.serialize(
            'json', [self.menu1, self.menu2, self.menu3])

        self.assertJSONEqual(
            str(response.content, encoding='utf8'), serialized_data)
