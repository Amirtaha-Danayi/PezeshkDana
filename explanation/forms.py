from django.forms import ModelForm
from.models import Explanation

class ExplanationForm(ModelForm):
    class Meta:
        model = Explanation
        fields = '__all__'