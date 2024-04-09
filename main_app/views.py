from django.shortcuts import render
from django.http import request
from django.views.generic.edit import CreateView, DeleteView
from .models import Dog

# Create your views here.

def home(request):
    return render(request, 'home.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {
        'dogs': dogs
    })

def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    return render(request, 'dogs/detail.html', {
        'dog': dog
    })

class DogCreate(CreateView):
    model = Dog
    fields = '__all__'

class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs'
