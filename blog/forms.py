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
        fields = ('rating', 'location', 'body')


class UserUpdateForm(forms.ModelForm):
    """
    Form class for the user profile update
    """
    email = forms.EmailField()

    class Meta:
        """Form fields"""
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']