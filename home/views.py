from django.shortcuts import render
from .models import Contact, Subscriber
from django.views import generic, View
from .forms import ContactForm, SubscriberForm
from django.shortcuts import (render, get_object_or_404,
                              reverse, redirect)


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def about(request):
    """ A view to return the about page """

    return render(request, 'home/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home/about.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'home/contact.html', context)

def new(request):
    if request.method == 'POST':
        sub = Subscriber(email=request.POST['email'], conf_num=random_digits())
        sub.save()
        return render(request, 'home/about.html')
