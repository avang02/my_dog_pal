from django.urls import reverse
from django.db import models

# Create your models here.

class Dog(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    neutered_sprayed = models.BooleanField(default=False)
    weight = models.FloatField()
    birthdate = models.DateField(null=True, blank=True)
    
    def __string__(self):
        return self.name
    




