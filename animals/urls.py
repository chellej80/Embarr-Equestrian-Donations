from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_animals, name='animals'),
    path('<int:animal_id>/', views.animal_detail, name='animal_detail'),
    path('add/', views.add_animal, name='add_animalS'),
]
