from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Animal, Category
from .forms import AnimalForm



# Create your views here.


def all_animals(request):
    """A view to show all Horses"""

    animals = Animal.objects.all()
    query = None
    categories = None
    

    if request.GET:
        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            animals = animals.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse("animals"))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            animals = animals.filter(queries)

    context = {
        "animals": animals,
        "search_term": query,
        "current_categories": categories,
    }

    return render(request, "animals/animals.html", context)


def animal_detail(request, animal_id):
    """A view to show individual animal details"""

    animal = get_object_or_404(Animal, pk=animal_id)

    context = {
        "animal": animal,
    }

    return render(request, "animals/animal_detail.html", context)


def add_animal(request):
    """ Add a animal to the store """
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added an Animal!')
            return redirect(reverse('add_animal'))
        else:
            messages.error(request, 'Failed to add an animal. Please ensure the form is valid.')
    else:
        form = AnimalForm()
    
    template = 'animals/add_animal.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
