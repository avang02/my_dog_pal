from django.shortcuts import render
from django.http import request
from django.views.generic.edit import CreateView
from .models import Dog

# Create your views here.

def home(request):
    return render(request, 'home.html')

class DogCreate(CreateView):
    model = Dog
    fields = '__all__'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog.id':self.id})