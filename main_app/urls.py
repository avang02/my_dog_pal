from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dogs/', views.dogs_index, name='index'),
    path('dogs/create', views.DogCreate.as_view(), name = 'dogs_create'),
]