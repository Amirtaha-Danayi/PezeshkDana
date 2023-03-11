from django.forms import ModelForm
from.models import Sickness

class SicknessForm(ModelForm):
    class Meta:
        model = Sickness
        fields = '__all__'