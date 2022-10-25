from django.contrib import admin
from .models import Animal, Category

# Register your models here.

class AnimalAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'donate',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
admin.site.register(Animal)
admin.site.register(Category)
