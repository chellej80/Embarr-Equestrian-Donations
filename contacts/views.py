from django.shortcuts import render
from .forms import ContactForm

"""
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/contact.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)

"""

def contactview(request):
    """ A view to return the contact page """

    return render(request, 'contacts/contact.html')
