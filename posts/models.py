from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Chatroom(models.Model):
    name = models.CharField(max_length=30)
    users = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Post(models.Model):
    post_text = models.TextField(max_length=140)
    post_image = models.ImageField(upload_to='post-img', blank=True, null=True)
    pub_date = models.DateTimeField('date posted', auto_now_add=True)
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    chatroom = models.ForeignKey(
        Chatroom, on_delete=models.CASCADE, related_name='posts', null=True)

    def __str__(self):
        return self.post_text

    def add_likes(self):
        self.likes += 1
        return self.likes

    class Meta:
        ordering = ['pub_date']
