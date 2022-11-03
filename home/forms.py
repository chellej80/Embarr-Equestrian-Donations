from django import forms
#from django.contrib.auth.models import User
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Submit Contact
    """
    class Meta:
        """Form fields"""
        model = Contact
        fields = ('location', 'body')
