from django.forms import ModelForm
from .models import DogCalculator

class DogcalculatorForm(ModelForm):
    class Meta:
        model = DogCalculator
        fields = ['ideal_weight', 'activity', 'servingspercup']

    