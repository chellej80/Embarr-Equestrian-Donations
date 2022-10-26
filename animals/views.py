from django.shortcuts import render, get_object_or_404
from .models import Animal

# Create your views here.


def all_animals(request):
    """ A view to show all products, including sorting and search queries """

    animals = Animal.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('animals'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'animals': animals,
        'search_term': query,
    }

    return render(request, 'animals/animals.html', context)

def animal_detail(request, animal_id):
    """ A view to show individual product details """

    animal = get_object_or_404(Animal, pk=animal_id)

    context = {
        'animal': animal,
    }

    return render(request, 'animals/animal_detail.html', context)
