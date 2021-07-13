from django.test import SimpleTestCase
from django.urls import reverse, resolve
from hotel.views import index, menu, OrderView, foodListing, Cart, Checkout


class TestUrls(SimpleTestCase):

    def test_index_url_is_resolves(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)
        print("Index page rendered!!")

    def test_menu_url_is_resolves(self):
        url = reverse('menu')
        self.assertEquals(resolve(url).func, menu)
        print("Menu page rendered!!")

    def test_food_listing_url_is_resolves(self):
        url = reverse('foodListing')
        self.assertEquals(resolve(url).func.view_class, foodListing)
        print("FoodListing page rendered!!")

    def test_cart_url_is_resolves(self):
        url = reverse('cart')
        self.assertEquals(resolve(url).func.view_class, Cart)
        print("Cart page rendered!!")

    def test_checkout_url_is_resolves(self):
        url = reverse('checkout')
        self.assertEquals(resolve(url).func.view_class, Checkout)
        print("Order placed successfully!!")

    def test_order_url_is_resolves(self):
        url = reverse('order')
        self.assertEquals(resolve(url).func.view_class, OrderView)
        print("Orders page rendered")