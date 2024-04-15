from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from .models import Dog, DogFood, FoodTrans, MyVet, Photo
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from math import pow
import uuid
import boto3
import os
import requests


def vet_search(request):
    vet_results = []
    if request.method == 'GET' and 'input' in request.GET:
        input_value = request.GET['input']
        input_type = 'textquery'
        fields = ['formatted_address', 'name', 'business_status', 'place_id']
        api_key = 'AIzaSyAUwpcXbJv7Jyb4_HJL7nYFVBQ7Xjv3CuA'

        url = f'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={input_value}&inputtype={input_type}&fields={fields}&key={api_key}'
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200 and data.get('status') == 'OK':
            vet_results = data.get('candidates', [])

    return render(request, 'vet_search.html', {'vet_results': vet_results})




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
    dogfood_id_list = dog.dogfood.all().values_list('id')
    dogfood_dog_doesnt_have = DogFood.objects.exclude(id__in=dogfood_id_list)
    foodtrans_id_list = dog.foodtrans.all().values_list('id')
    foodtrans_dog_doesnt_have = FoodTrans.objects.exclude(id__in=foodtrans_id_list)

    ideal_weight = request.POST.get('ideal-weight')
    activity = request.POST.get('activity')
    servingspercup = request.POST.get('servingspercup')
    kcal_per_day = None
    if ideal_weight != None and activity != None: 
        kcal_per_day = round(pow(float(ideal_weight), 0.75) * float(activity))
    
    return render(request, 'dogs/detail.html', {
        'dog': dog,
        'dogfood': dogfood_dog_doesnt_have,
        'foodtrans': foodtrans_dog_doesnt_have,
        'ideal_weight': ideal_weight,
        'activity': activity,
        'servingspercup': servingspercup,
        'kcal_per_day': kcal_per_day,
    })



class DogCreate(LoginRequiredMixin, CreateView):
    model = Dog
    fields = ['name', 'id_number', 'breed', 'neutered_spayed', 'weight', 'birthdate', 'img_url']
    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class DogDelete(LoginRequiredMixin, DeleteView):
    model = Dog
    success_url = '/dogs'

class DogUpdate(LoginRequiredMixin, UpdateView):
    model = Dog
    fields = ['name', 'id_number', 'breed', 'neutered_spayed', 'weight', 'birthdate', 'img_url']

@login_required
def dogfood_index(request):
    dogfood = DogFood.objects.filter(user=request.user)
    return render(request, 'dogfood/index.html', {
        'dogfood': dogfood
    })

class DogFoodCreate(LoginRequiredMixin, CreateView):
    model = DogFood
    fields = ['name', 'kcalperserving', 'gramperserving']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DogFoodDelete(LoginRequiredMixin, DeleteView):
    model = DogFood
    success_url = '/dogfood/'

class DogFoodUpdate(LoginRequiredMixin, UpdateView):
    model = DogFood
    fields = ['name', 'kcalperserving', 'gramperserving']

@login_required
def dogfood_detail(request, pk):
    dogfood = DogFood.objects.get(id=pk)
    return render(request, 'dogfood/detail.html', {
        'dogfood': dogfood,
    })

@login_required
def assoc_dogfood(request, dog_id, dogfood_id):
    Dog.objects.get(id=dog_id).dogfood.add(dogfood_id)
    return redirect('detail', dog_id=dog_id)

@login_required
def unassoc_dogfood(request, dog_id, dogfood_id):
    Dog.objects.get(id=dog_id).dogfood.remove(dogfood_id)
    return redirect('detail', dog_id=dog_id)

@login_required
def foodtrans_index(request):
    foodtrans = FoodTrans.objects.filter(user=request.user)
    return render(request, 'foodtrans/index.html', {
        'foodtrans': foodtrans
    })

class FoodTransCreate(LoginRequiredMixin, CreateView):
    model = FoodTrans
    fields = ['name', 'current_food', 'new_food', 'meals_a_day', 'start_date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class FoodTransDelete(LoginRequiredMixin, DeleteView):
    model = FoodTrans
    success_url = '/foodtrans/'

class FoodTransUpdate(LoginRequiredMixin, UpdateView):
    model = FoodTrans
    fields = ['name', 'current_food', 'new_food', 'meals_a_day', 'start_date']

@login_required 
def foodtrans_detail(request, pk):
    foodtrans = FoodTrans.objects.get(id=pk)
    return render(request, 'foodtrans/detail.html', {
        'foodtrans': foodtrans,
    })

@login_required
def assoc_foodtrans(request, dog_id, foodtrans_id):
    Dog.objects.get(id=dog_id).foodtrans.add(foodtrans_id)
    return redirect('detail', dog_id=dog_id)

@login_required
def unassoc_foodtrans(request, dog_id, foodtrans_id):
    Dog.objects.get(id=dog_id).foodtrans.remove(foodtrans_id)
    return redirect('detail', dog_id=dog_id)

@login_required
def myvet_index(request):
    myvet = MyVet.objects.filter(user = request.user)
    return render(request, 'myvet/index.html', {
        'myvet': myvet
    })

class MyVetCreate(LoginRequiredMixin, CreateView):
    model = MyVet
    fields = ['name', 'clinic_name','preferred_doctor', 'phone_number', 'email']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MyVetDelete(LoginRequiredMixin, DeleteView):
    model =MyVet
    success_url = '/myvet/'

class MyVetUpdate(LoginRequiredMixin, UpdateView):
    model = MyVet
    fields = ['name', 'clinic_name','preferred_doctor', 'phone_number', 'email']

def myvet_detail(request, pk):
    myvet = MyVet.objects.get(id=pk)
    return render(request, 'myvet/detail.html', {
        'myvet': myvet,
    })
    
def secretkey(request):
    secrect_key = os.environ['SECRET_KEY']

def add_photo(request, dog_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, dog_id=dog_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', dog_id=dog_id)






