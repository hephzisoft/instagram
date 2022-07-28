
from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    avatar = models.ImageField(default="avatar.svg", null=True)
    email = models.EmailField(null=True)
    bio = models.TextField(null=True)


class Feed(models.Model):
    host  = models.ForeignKey(User, on_delete=models.CASCADE)
    image_feed = models.FileField(upload_to="upload")
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    
    class Meta:
        ordering = ['-updated', '-created']


    def __str__(self):
        return self.description[0:50]

class Comment(models.Model):
    feed = models.ForeignKey(Feed,on_delete=models.CASCADE)