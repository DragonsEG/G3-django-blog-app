from django.test import TestCase, Client
from django.urls import reverse
from BlogApplication.views import *
from django.utils import timezone


class TestView(TestCase):

    def testLoginView(self):
        client = Client()
        response = client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'BlogApplication/LoginPage.html')

    def testIndex(self):
        client = Client()
        response = client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'BlogApplication/Home.html')

    def testRenderAdd(self):
        client = Client()
        response = client.get(reverse('add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'BlogApplication/Add.html')

    def testEditPost(self):
        client = Client()
        # Create and a User (author) object
        authorU = User.objects.create(
            username="testUser", password="testPassword")
        # Create a BlogPost object with ID 500 for testing
        BlogPost.objects.create(id=500, author=authorU, title="Test Post",
                                content="Test Content", pupDate=timezone.now())
        response = client.get(reverse('edit', args=[500]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'BlogApplication/Edit.html')

    def testDeletePost(self):
        client = Client()
        # Create and a User (author) object
        authorU = User.objects.create(
            username="testUser", password="testPassword")
        # Create a BlogPost object with ID 500 for testing
        BlogPost.objects.create(id=500, author=authorU, title="Test Post",
                                content="Test Content", pupDate=timezone.now())
        response = client.get(reverse('delete', args=[500]))
        # Check that the response status code is a redirect (302)
        self.assertEqual(response.status_code, 302)
        # Check that the response redirects to the "posts" URL
        self.assertTemplateNotUsed(response, reverse('posts'))
        # Check that the BlogPost with ID 500 no longer exists
        self.assertFalse(BlogPost.objects.filter(id=500).exists())

    def testAddPost(self):
        client = Client()
        response = client.get(reverse('addPost'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'BlogApplication/Add.html')

    def testAddComment(self):
        client = Client()
        # Create and a User (author) object
        authorU = User.objects.create(
            username="testUser", password="testPassword")
        # Create a BlogPost object with ID 500 for testing
        BlogPost.objects.create(id=500, author=authorU, title="Test Post",
                                content="Test Content", pupDate=timezone.now())
        response = client.get(reverse('addComment', args=[500]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'BlogApplication/Details.html')

    def testPostDetails(self):
        client = Client()
        # Create and a User (author) object
        authorU = User.objects.create(
            username="testUser", password="testPassword")
        # Create a BlogPost object with ID 500 for testing
        BlogPost.objects.create(id=500, author=authorU, title="Test Post",
                                content="Test Content", pupDate=timezone.now())
        response = client.get(reverse('details', args=[500]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'BlogApplication/Details.html')
