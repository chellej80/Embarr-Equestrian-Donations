from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Set blog status


STATUS = ((0, "Draft"), (1, "Publish"))


class Post(models.Model):
    """
    Model for the creation & management of the Service posts
    """

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="test_posts"
    )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """order by created date/time"""

        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Class Comment model that creates and saves the comment in the DB
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    location = models.CharField(max_length=80, default="")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    class Meta:
        """order by created date/time"""

        ordering = ["created_on"]

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)

    def get_absolute_url(self):
        """Sets absolute URL"""
        return reverse("post_detail", args=[self.post.slug])
