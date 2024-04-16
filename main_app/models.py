from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DogFood(models.Model):
    name = models.CharField(max_length=50)
    kcalperserving = models.IntegerField()
    gramperserving = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dogfood_detail', kwargs={'pk': self.id})
    
class MyVet(models.Model):
    name = models.CharField(max_length=50)
    clinic_name = models.CharField(max_length=50)
    preferred_doctor = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __string__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myvet_detail', kwargs={'pk':self.id})  
    
class FoodTrans(models.Model):
    name = models.CharField(max_length=50)
    current_food = models.ForeignKey(DogFood, on_delete=models.CASCADE)
    new_food = models.CharField(max_length=50)
    meals_a_day = models.IntegerField()
    start_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('foodtrans_detail', kwargs={'pk':self.id})
    
class Dog(models.Model):
    name = models.CharField(max_length=50)
    id_number = models.IntegerField(null=True, blank=True)
    breed = models.CharField(max_length=50)
    neutered_spayed = models.BooleanField(default=False)
    weight = models.FloatField()
    birthdate = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dogfood = models.ManyToManyField(DogFood)
    foodtrans = models.ManyToManyField(FoodTrans)
    vet = models.ManyToManyField(MyVet)
    img_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id':self.id})
    
class Photo(models.Model):
    url = models.CharField(max_length=200)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for dog_id: {self.dog_id} @{self.url}"



