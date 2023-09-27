from django.test import TestCase
from BlogApplication.models import *
from django.utils import timezone
from datetime import datetime


class TestModel(TestCase):
    def testBlogPost(self):

        # Create and a User (author) object
        authorU = User.objects.create(
            username="testUser", password="testPassword")
        # Create a BlogPost object with ID 500 for testing
        blogPost = BlogPost.objects.create(id=500, author=authorU, title="Test Post",
                                           content="Test Content", pupDate=timezone.now())
        self.assertEqual(blogPost.title, "Test Post")
        self.assertEqual(blogPost.author, authorU)
        self.assertEqual(blogPost.content, "Test Content")
        # self.assertEqual(blogPost.pupDate, timezone.now())

    def testComment(self):

        # Create and a User (author) object
        authorU = User.objects.create(
            username="testUser", password="testPassword")
        # Create a BlogPost object with ID 500 for testing
        blogPost = BlogPost.objects.create(id=500, author=authorU, title="Test Post",
                                           content="Test Content", pupDate=timezone.now())
        comment = Comment.objects.create(
            id=600, author=authorU, content="Test Content", blogPostID=blogPost, pupDate=timezone.now())
        self.assertEqual(comment.blogPostID, blogPost)
        self.assertEqual(comment.author, authorU)
        self.assertEqual(comment.content, "Test Content")
        # self.assertEqual(comment.pupDate, timezone.now())
