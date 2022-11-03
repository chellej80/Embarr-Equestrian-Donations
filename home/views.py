from django.shortcuts import render
from .models import Contact

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def about(request):
    """ A view to return the index page """

    return render(request, 'home/about.html')

def contact_form(request):

    model = Contact
    #template_name = 'blog/edit_comment.html'
    form_class = ContactForm
    success_message = 'Your comment was updated'