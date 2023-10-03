from django.test import SimpleTestCase
from django.urls import reverse, resolve
from BlogApplication.views import *


class TestUrls(SimpleTestCase):

    def testLogin(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, loginView)

    def testPosts(self):
        url = reverse('posts')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)

    def testEdit(self):
        url = reverse('edit', args=[50])
        print(resolve(url))
        self.assertEquals(resolve(url).func, editPost)

    def testDelete(self):
        url = reverse('delete', args=[500])
        print(resolve(url))
        self.assertEquals(resolve(url).func, deletePost)

    def testDetails(self):
        url = reverse('details', args=[500])
        print(resolve(url))
        self.assertEquals(resolve(url).func, postDetails)

    def testAddPost(self):
        url = reverse('addPost')
        print(resolve(url))
        self.assertEquals(resolve(url).func, addPost)

    def testAddComment(self):
        url = reverse('addComment', args=[500])
        print(resolve(url))
        self.assertEquals(resolve(url).func, addComment)
