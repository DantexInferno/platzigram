from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  website = models.URLField(max_length=255, blank=True)
  biography = models.TextField(max_length=155, blank=True)
  phone = models.CharField(max_length=30, blank=True)
  picture = models.ImageField(upload_to='users/picture', blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.user.username