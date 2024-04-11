from .models import Dog

def dogs_list(request):
    if request.user.is_authenticated:
        dogs = Dog.objects.filter(user=request.user)
    else:
        dogs = None
    return {'dogs': dogs}