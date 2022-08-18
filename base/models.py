
from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    avatar = models.ImageField(default="avatar.svg", null=True)
    email = models.EmailField(null=True)
    bio = models.TextField(null=True)


class Feed(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    image_feed = models.FileField(upload_to="upload")
    description = models.TextField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)


    
    class Meta:
        ordering = ['-updated', '-created']


    def __str__(self):
        return self.description[0:50]

# class Comment(models.Model):
#     feed = models.ForeignKey(Feed,on_delete=models.CASCADE)
#     comment = models.ManyToManyField(User, related_name='comment')
#     comment_body = models.TextField(null=True)


class Like(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name='feed_likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_likes')

    def __str__(self):
        return self.feed.description[0:50]