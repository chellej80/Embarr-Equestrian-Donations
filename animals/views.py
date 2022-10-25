from django.shortcuts import render
from .models import Animal

# Create your views here.

def all_animals(request):
    """ A view to show all products, including sorting and search queries """

    animals = Animal.objects.all()

    context = {
        'animals': animals,
    }

    return render(request, 'animals/animals.html', context)
