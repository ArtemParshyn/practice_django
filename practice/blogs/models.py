from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.CharField(max_length=64)
    blogs = models.JSONField(default=dict, blank=True, null=True)


class Blog(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=240)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.JSONField(default=dict, blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now_add=True)
