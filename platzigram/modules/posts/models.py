from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

  user = models.ForeignKey(User, on_delete=models.CASCADE)
  profile = models.ForeignKey('Users.Profile', on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  photo = models.ImageField(upload_to="posts/photos")

  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)

  def __str__(self):
    return f"{self.title} by @{self.user.username}"