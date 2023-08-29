from django.test import TestCase
from django.urls import reverse
import json
from restaurant.models import *


class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of the Menu model
        MenuItem.objects.create(title='Burger', price=40, inventory=100)
        MenuItem.objects.create(title='Shawarma', price=20, inventory=100)
        MenuItem.objects.create(title='Pizza', price=50, inventory=100)

    def test_getall(self):
        response = self.client.get(reverse('menu-list'))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Serialize the expected data
        expected_data = [
            {"title": "Burger", "price": 40, "inventory": 100},
            {"title": "Shawarma", "price": 20, "inventory": 100},
            {"title": "Pizza", "price": 50, "inventory": 100}
        ]

        # Deserialize the response content
        response_data = json.loads(response.content)

        # Compare the expected data with the response data
        self.assertEqual(expected_data, response_data)
