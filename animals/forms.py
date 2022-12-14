from django import forms
from .models import Animal, Category


class AnimalForm(forms.ModelForm):

    class Meta:
        model = Animal
        fields = ('category', 'sku', 'name', 'description',
                  'donation', 'image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
