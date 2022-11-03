from django.shortcuts import render, redirect, reverse,  get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Animal, Category
 

# Create your views here.


def all_animals(request):
    """ A view to show all Horses """

    animals = Animal.objects.all()
    query = None
    categories = None
    paginate_by = 6

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            animals = animals.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('animals'))
                
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            animals = animals.filter(queries)

    context = {
        'animals': animals,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'animals/animals.html', context)

def animal_detail(request, animal_id):
    """ A view to show individual product details """

    animal = get_object_or_404(Animal, pk=animal_id)

    context = {
        'animal': animal,
    }

    return render(request, 'animals/animal_detail.html', context)
