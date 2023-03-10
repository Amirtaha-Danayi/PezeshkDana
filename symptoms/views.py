from django.shortcuts import render
from django.views import generic
from .models import Symptoms
from django.urls import reverse_lazy

class SymptomsList(generic.ListView):
    model = Symptoms
    template_name = 'symptoms/symptoms_list.html'
    context_object_name = 'symptoms'


class SymptomsDetail(generic.DetailView):
    model = Symptoms
    template_name = 'symptoms/symptoms_dtail.html'


class SymptomsCreate(generic.CreateView):
    model = Symptoms
    fields = ['title', 'english_title', 'definition', 'classification', 'mechanism', 'pathophysiology', 'related', 'diagnostic_value', 'clinical_features', 'diagnosis', 'epidemiology', 'management', 'etiology', 'cause', 'gallery']
    template_name = 'symptoms/symptoms_crete.html'


class SymptomsUpdate(generic.UpdateView):
    model = Symptoms
    fields = ['title', 'english_title', 'definition', 'classification', 'mechanism', 'pathophysiology', 'related', 'diagnostic_value', 'clinical_features', 'diagnosis', 'epidemiology', 'management', 'etiology', 'cause', 'gallery']
    template_name = 'symptoms/symptoms_update.html'

class SymptomsDelete(generic.DeleteView):
    model = Symptoms
    template_name = 'symptoms/symptoms_delete.html'
    success_url = reverse_lazy('symptoms_list')
