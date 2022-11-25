from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Submit Contact
    """
    class Meta:
        """Form fields"""
        model = Contact
        fields = ('County', 'Town', 'Eircode', 'Description', 'Condition')
