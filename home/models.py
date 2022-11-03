from django.db import models


class Contact(models.Model):
    """
    Class Contact model that creates and saves the comment in the DB
    """
    location = models.CharField(max_length=100, default='')
    body = models.TextField()
    photo = models.ImageField(null=True, blank=True)
    #image_url = models.URLField(max_length=1024, null=True, blank=True)