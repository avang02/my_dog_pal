from .models import Dog

def dogs_list(request):
    dogs = Dog.objects.all()
    return {'dogs': dogs}