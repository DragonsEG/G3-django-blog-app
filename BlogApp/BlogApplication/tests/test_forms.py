from django.test import TestCase
from BlogApplication.forms import *

class TestForms(TestCase):
    def testBlogPostFormValidData(self):
        form = BlogPostForm(data={
            'title': 'Test Post',
            'content': 'Test Content',
        })
        self.assertTrue(form.is_valid())

    def testBlogPostFormEmptyData(self):
        form = BlogPostForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)

    def testCommentFormValidData(self):
        form = CommentForm(data={
            'content': 'Test Comment',
        })
        self.assertTrue(form.is_valid())

    def testCommentFormEmptyData(self):
        form = CommentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
