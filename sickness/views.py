from django.shortcuts import render
from django.views import generic
from .models import Sickness
from django.urls import reverse_lazy


class SicknessList(generic.ListView):
    model = Sickness
    template_name = 'sickness/sickness_list.html'
    context_object_name = 'sickness'


class SicknessDetail(generic.DetailView):
    model = Sickness
    template_name = 'sickness/sickness_detail.html'


class SicknessCreate(generic.CreateView):
    model = Sickness
    fields = ['title', 'english_title', 'summary', 'definition', 'classification', 'pathophysiology', 'differential_diagnoses', 'clinical_features', 'epidemiology', 'etiology', 'diagnosis', 'management', 'treatment', 'risk_factors', 'complications', 'prognosis', 'prevention', 'other_names', 'gallery']
    template_name = 'sickness/sickness_create.html'



class SicknessUpdate(generic.UpdateView):
    model = Sickness
    fields = ['title', 'english_title', 'summary', 'definition', 'classification', 'pathophysiology',
              'differential_diagnoses', 'clinical_features', 'epidemiology', 'etiology', 'diagnosis', 'management',
              'treatment', 'risk_factors', 'complications', 'prognosis', 'prevention', 'other_names', 'gallery']
    template_name = 'sickness/sickness_update.html'

class SicknessDelete(generic.DeleteView):
    model = Sickness
    template_name = 'sickness/sickness_delete.html'
    success_url = reverse_lazy('sickness_list')