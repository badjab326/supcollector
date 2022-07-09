from django.forms import ModelForm
from .models import Taking

class TakingForm(ModelForm):
    class Meta:
        model = Taking
        fields = ['date', 'time']