from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import custRegister


class TestUrls(SimpleTestCase):

    def test_custRegister_url_is_resolves(self):
        url = reverse('custRegister')
        self.assertEquals(resolve(url).func, custRegister)
        print("CustRegisteration working fine!!")