from  django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, auth
import json

class TestCustRegViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        if User.objects.filter(username='spoorti').exists():
            print("Username taken")
        elif User.objects.filter(email='spo@gmail.com').exists():
            print("Email already exists!!")
        else:
            User.objects.create(
                username='nakadi',
                email ='nak@gmail.com',
                password='starnaK@8'
            )
            print("User registered sucessfully!!")

    def test_cust_register_POST(self):
        url = reverse('custRegister')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        qs = User.objects.all()
        self.assertEqual(qs.count(),1)
        # print("User registered sucessfully!!")

# class TestCustLogin(TestCase):

    # def setUp(self):
    #     self.Client = Client()
    #     user = auth.authenticate(
    #         username='nakadi',
    #         password='starnaK@8'
        # )
        # qs = auth.login(request, user)
        # self.assertEqual(qs.count(),1)

    # def test_cust_login_POST(self):
    #     url2 = reverse('custLogin')
    #     response = self.client.get(url2)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response,'custLogin.html')
    #     # qs = auth.login(request, user)
    #     # self.assertEqual(qs.count(),1)
    #     print("User registered sucessfully!!")
       