from django.forms import ModelForm
from.models import Symptoms

class SymptomsForm(ModelForm):
    class Meta:
        model = Symptoms
        fields = '__all__'