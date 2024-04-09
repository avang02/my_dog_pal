from django.urls import reverse
from django.db import models

# Create your models here.

class Dog(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    neutered_spayed = models.BooleanField(default=False)
    weight = models.FloatField()
    birthdate = models.DateField(null=True, blank=True)
    
    def __string__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id':self.id})



