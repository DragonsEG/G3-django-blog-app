from django.contrib.auth.models import AbstractUser
from django.db import models
from BlogApplication.models import Company  # Import your Company model

class CustomUser(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)

# In your project settings, set AUTH_USER_MODEL to your custom user model:
AUTH_USER_MODEL = 'Users.CustomUser'
