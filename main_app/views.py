from django.shortcuts import render
from django.http import request
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Dog

# Create your views here.

def home(request):
    return render(request, 'home.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {
        'dogs': dogs
    })

class DogCreate(CreateView):
    model = Dog
    fields = '__all__'

