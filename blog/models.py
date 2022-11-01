from django.db import models

"""Models Imports"""
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Set blog status


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)



class Blog(models.Model):
    """
    Model for the creation & management of the Service posts
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='test_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """order by created date/time"""
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Class review model that creates and saves the comment in the DB
    """

    
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,
                             related_name='reviews')
    name = models.CharField(max_length=80)
    location = models.CharField(max_length=80, default='e.g Dublin')
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    class Meta:
        """order by created date/time"""
        ordering = ['created_on']

    def __str__(self):
        return 'Review {} by {}'.format(self.body, self.name)

    def get_absolute_url(self):
        """Sets absolute URL"""
        return reverse('blog_detail', args=[self.blog.slug])
