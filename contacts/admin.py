from django.contrib import admin
from .models import Contact

#admin.site.register(Contact)

@admin.register(Contact)


class ContactAdmin(admin.ModelAdmin):
    """
    Admin Class for the management of Blog posts

    """
    list_display = ('email', 'subject', 'message')
    search_fields = ['email', 'subject']
    