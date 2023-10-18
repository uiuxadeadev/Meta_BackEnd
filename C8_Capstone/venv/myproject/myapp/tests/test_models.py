from django.test import TestCase
from ..models import MenuItem

# TestCase class


class MenuItemTest(TestCase):
    # def test_get_item(self):
    #     item = MenuItem.objects.create(
    #         title=2, price=80)
    # self.assertEqual(item, "1")
    def test_get_item(self):
        item = MenuItem.objects.create(
            title="IceCream", price=80)
        self.assertEqual(item.title, "IceCream")
        self.assertEqual(item.price, 8)
