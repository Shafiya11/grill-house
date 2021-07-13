from  django.test import TestCase, Client
from django.urls import reverse
from hotel.models import Events, Item, FoodListing, Order
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.event_url = reverse('index')
        self.item_url = reverse('menu')
        self.food_list_url = reverse('foodListing')

    def test_events_GET(self):
        response = self.client.get(self.event_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_item_GET(self):
        response = self.client.get(self.item_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')
    