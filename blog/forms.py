"""Forms Imports"""
from django import forms
from django.contrib.auth.models import User
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Submit Form for the Comments
    """
    class Meta:
        """Form fields"""
        model = Comment
        fields = ('location', 'body')


