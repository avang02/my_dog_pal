from django.contrib import admin
from .models import Dog, DogFood, DogCalculator, FoodTrans, MyVet, Photo

# Register your models here.

admin.site.register(Dog)
admin.site.register(DogFood)
admin.site.register(DogCalculator)
admin.site.register(FoodTrans)
admin.site.register(MyVet)
admin.site.register(Photo)
