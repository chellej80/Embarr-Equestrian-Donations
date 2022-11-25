"""Admin Imports"""
from django import forms
from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('County', 'Town', 'Eircode', 'Description')





