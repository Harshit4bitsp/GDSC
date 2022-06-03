from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    heading = models.CharField(max_length=100)

    content = models.TextField(null=True, blank=True)

    tags = TaggableManager(blank=True)
