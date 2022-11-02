from django.contrib import admin
from django.urls import path
from contacts import views 

urlpatterns = [
    path('', views.contact_view, name='contact_view'),
]