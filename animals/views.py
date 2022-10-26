from django.shortcuts import render, get_object_or_404
from .models import Animal

# Create your views here.


def all_animals(request):
    """ A view to show all products, including sorting and search queries """

    animals = Animal.objects.all()

    context = {
        'animals': animals,
    }

    return render(request, 'animals/animals.html', context)

def animal_detail(request, animal_id):
    """ A view to show individual product details """

    animal = get_object_or_404(Animal, pk=animal_id)

    context = {
        'animal': animal,
    }

    return render(request, 'animals/animal_detail.html', context)
