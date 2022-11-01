""" view Imports"""
from django.views import generic, View
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import (render, get_object_or_404,
                              reverse, redirect)
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import Post, Comment
# from django.contrib.auth.models import User
#from .forms import commentForm, UserUpdateForm
# from django.urls import reverse_lazy


class PostList(generic.ListView):
    """
    This class is for the display of the service posts
    """
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/posts.html'
    paginate_by = 3


class PostDetail(View):
    """
    This class is for the display of the service post detail
    """

    def get(self, request, slug):
        """
        This Function is used to retrieve the service post detail and comments
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
            },
        )

    def post(self, request, slug):
        """
        This Function is used for the comments of posts
        """

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        comment_form = commentForm(data=request.POST)
        new_comment = None

        # comment posted
        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
        else:
            comment_form = commentForm()

        return render(request, 'post_detail.html',
                      {'post': post,
                       'comments': comments,
                       'comment_form': comment_form,
                       'new_comment': new_comment})


