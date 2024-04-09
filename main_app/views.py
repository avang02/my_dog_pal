from django.shortcuts import render, redirect
from django.http import request
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Dog
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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

class DogUpdate(UpdateView):
    model = Dog
    fields = '__all__'

def signup(request):
    error_message=''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
