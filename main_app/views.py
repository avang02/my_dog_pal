from django.shortcuts import render, redirect
from django.http import request
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from .models import Dog, DogFood
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required
def dogs_index(request):
    dogs = Dog.objects.filter(user=request.user)
    return render(request, 'dogs/index.html', {
        'dogs': dogs
    })

@login_required
def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    return render(request, 'dogs/detail.html', {
        'dog': dog
    })


class DogCreate(LoginRequiredMixin, CreateView):
    model = Dog
    # fields = '__all__'
    fields = ['name', 'breed', 'neutered_spayed', 'weight', 'birthdate']
    

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class DogDelete(LoginRequiredMixin, DeleteView):
    model = Dog
    success_url = '/dogs'

class DogUpdate(LoginRequiredMixin, UpdateView):
    model = Dog
    fields = ['name', 'breed', 'neutered_spayed', 'weight', 'birthdate']

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

class DogFoodCreate(LoginRequiredMixin, CreateView):
    model = DogFood
    fields = ['name', 'kcalperserving', 'gramperserving', 'current_food', 'new_food']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class DogFoodList(LoginRequiredMixin, ListView):
    model = DogFood

class DogFoodDelete(LoginRequiredMixin, DeleteView):
    model = DogFood
    success_url = '/dogfood/'

class DogFoodUpdate(LoginRequiredMixin, UpdateView):
    model = DogFood
    fields = '__all__'
    

@login_required
def dogfood_detail(request, pk):
    dogfood = DogFood.objects.get(id=pk)
    return render(request, 'dogfood/detail.html', {
        'dogfood': dogfood
    })


@login_required
def assoc_dogfood(request, dog_id, dogfood_id):
    Dog.objects.get(id=dog_id).dogfood.add(dogfood_id)
    return redirect('detail', dog_id=dog_id)