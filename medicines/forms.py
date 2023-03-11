from django.forms import ModelForm
from.models import Medicines

class MedicinesForm(ModelForm):
    class Meta:
        model = Medicines
        fields = '__all__'