# /blogs/models.py
from django.db import models
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    text = models.TextField()

    """ Takes object and returns it as a string """
    def __str__ (self):
        return self.title

    """ Sends user back to path specified """
    def get_absolute_url(self):
        return reverse('home')