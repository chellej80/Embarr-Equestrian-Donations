from django.shortcuts import render
from .models import Contact
from django.views import generic, View
from .forms import ContactForm
from django.shortcuts import (render, get_object_or_404,
                              reverse, redirect)

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def about(request):
    """ A view to return the about page """

    return render(request, 'home/about.html')


def contact_view(request):
    """ A view to return the Welfare report form page """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            photo = form.cleaned_data.get("fields")
            form.save()
            
            return render(request, 'home/about.html')
    form = ContactForm()
    context = {'form': form}

    return render(request, 'home/contact.html', context)