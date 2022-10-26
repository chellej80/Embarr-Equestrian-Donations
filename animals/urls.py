from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_animals, name='animals')
    path('<animal_id>', views.animal_detail, name='animal_detail'),
]
