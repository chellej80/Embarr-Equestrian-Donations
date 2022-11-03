from django.db import models


class Contact(models.Model):
    """
    Class Contact model that creates and saves the comment in the DB
    """
    location = models.CharField(max_length=100, default='')
    body = models.TextField()
    