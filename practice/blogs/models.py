from django.db import models


# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=64)
    bio = models.CharField(max_length=64)
    blogs = models.JSONField(default=None, null=True)


class Blog(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=240)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.JSONField(default=None, null=True)
    Postdate = models.DateField(auto_now_add=True)


class Comment(models.Model):
    Blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Postdate = models.DateField(auto_now_add=True)
