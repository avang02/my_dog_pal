from django.forms import ModelForm
from .models import DogCalculator

class DogcalculatorForm(ModelForm):
    class Meta:
        model = DogCalculator
        fields = ['weight', 'activity', 'servingspercup']