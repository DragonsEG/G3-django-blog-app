from django.test import TestCase, Client
from django.urls import reverse
from Users.views import *
from django.utils import timezone
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from BlogApplication.views import *
from django.contrib.auth import views as auth_view
from Users.models import *
from datetime import datetime

# Create your tests here.


class TestViews(TestCase):
    def testSignUp(self):
        client = Client()
        response = client.get(reverse('userSignUp'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'BlogApplication/Signup.html')


class TestURLs(SimpleTestCase):
    def testLogin(self):
        url = reverse('userSignUp')
        print(resolve(url))
        self.assertEquals(resolve(url).func, signUp)

    def testLogout(self):
        url = reverse('userLogout')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, auth_view.LogoutView)
