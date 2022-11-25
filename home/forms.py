from django import forms
from .models import Contact, Subscriber


class ContactForm(forms.ModelForm):
    """
    Submit Contact
    """
    class Meta:
        """Form fields"""
        model = Contact
        fields = ('County', 'Town', 'Eircode', 'Description', 'Condition')

class SubscriberForm(forms.Form):
    email = forms.EmailField(label='Your email',
                             max_length=100,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))