from django.db import models
from django.contrib.auth.models import User


class BlogCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE) ## ID (numeric)
    title = models.CharField(max_length=200)
    content = models.TextField()
    pupDate = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, blank=True)
    draft = models.BooleanField(default=False)

    class Meta:
        ordering = ['-pupDate']

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    blogPostID = models.ForeignKey(BlogPost, on_delete= models.CASCADE)
    content = models.TextField()
    pupDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username}"





