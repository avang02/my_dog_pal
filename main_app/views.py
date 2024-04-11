from django.shortcuts import render, redirect
from django.http import request
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from .models import Dog, DogFood, FoodTrans, MyVet
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
    id_list = dog.dogfood.all().values_list('id')
    dogfood_dog_doesnt_have = DogFood.objects.exclude(id__in=id_list)
    return render(request, 'dogs/detail.html', {
        'dog': dog,
        'dogfood': dogfood_dog_doesnt_have
    })


class DogCreate(LoginRequiredMixin, CreateView):
    model = Dog
    fields = ['name', 'breed', 'neutered_spayed', 'weight', 'birthdate', 'img_url' ]
    

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
    fields = ['name', 'kcalperserving', 'gramperserving']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
# class DogFoodList(LoginRequiredMixin, ListView):
#         model = DogFood
@login_required
def dogfood_index(request):
    dogfood = DogFood.objects.filter(user=request.user)
    return render(request, 'dogfood/index.html', {
        'dogfood': dogfood
    })

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

@login_required
def unassoc_dogfood(request, dog_id, dogfood_id):
    Dog.objects.get(id=dog_id).dogfood.remove(dogfood_id)
    return redirect('detail', dog_id=dog_id)

class FoodTransCreate(LoginRequiredMixin, CreateView):
    model = FoodTrans
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
@login_required 
def foodtrans_detail(request, pk):
    foodtrans = FoodTrans.objects.get(id=pk)
    return render(request, 'foodtrans/detail.html', {
        'foodtrans': foodtrans,
    })

class FoodTransList(LoginRequiredMixin, ListView):
    model = FoodTrans

class FoodTransDelete(LoginRequiredMixin, DeleteView):
    model = FoodTrans
    success_url = '/foodtrans/'

class FoodTransUpdate(LoginRequiredMixin, UpdateView):
    model = FoodTrans
    fields = '__all__'

class MyVetCreate(LoginRequiredMixin, CreateView):
    model = MyVet
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class MyVetList(LoginRequiredMixin, ListView):
    model = MyVet

def myvet_detail(request, pk):
    myvet = MyVet.objects.get(id=pk)
    return render(request, 'myvet/detail.html', {
        'myvet': myvet,
    })

class MyVetDelete(LoginRequiredMixin, DeleteView):
    model =MyVet
    success_url = '/myvet/'

class MyVetUpdate(LoginRequiredMixin, UpdateView):
    model = MyVet
    fields = '__all__'
