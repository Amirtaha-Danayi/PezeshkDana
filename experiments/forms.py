from django.forms import ModelForm
from.models import Experiments

class ExperimentsForm(ModelForm):
    class Meta:
        model = Experiments
        fields = '__all__'