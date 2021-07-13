from django.test import TestCase
from hotel.models import Item, Events, FoodListing, Order

from django.test.testcases import TestCase


class TestItemModels(TestCase):

    def setUp(self):
        print('Setup activity for item')
        Item.objects.create(
            item_img = '',
            item_name='Desert'
        )
        
        print("Item created!!")

    def test_item_created(self):
        qs = Item.objects.all()
        self.assertEqual(qs.count(),1)

class TestEventsModels(TestCase):
    
    def setUp(self):
        print('Setup activity for event')
        Events.objects.create(
            event_id = 12,
            event_img = '',
            event_name ='New Year Event',
            event_desc = 'The new year theme party.'
        )
        print("Event created!!")

    def test_event_created(self):
        qs = Events.objects.all()
        self.assertEqual(qs.count(),1)