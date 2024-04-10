from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DogFood(models.Model):
    name = models.CharField(max_length=50)
    kcalperserving = models.IntegerField()
    gramperserving = models.IntegerField()
    current_food = models.CharField(max_length=50)
    new_food = models.CharField()

    def __string__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dogfood_detail', kwargs={'pk': self.id})


class Dog(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    neutered_spayed = models.BooleanField(default=False)
    weight = models.FloatField()
    birthdate = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dogfood = models.ManyToManyField(DogFood)
    
    def __string__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id':self.id})
    






