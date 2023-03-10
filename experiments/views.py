from django.shortcuts import render
from django.views import generic
from .models import Experiments
from django.urls import reverse_lazy


class ExperimentsList(generic.ListView):
    model = Experiments
    template_name = 'experiments/experiments_list.html'
    context_object_name = 'experiments'

class ExperimentsDetail(generic.DetailView):
    model = Experiments
    template_name = 'experiments/experiments_detail.html'


class ExperimentsCreate(generic.CreateView):
    model = Experiments
    fields = ['name', 'english_name', 'natural_range', 'physiopathology', 'reasons_for', 'change', 'interpretation', 'quick_interpretation', 'differential_diagnoses', 'false_results', 'references', 'gallery']
    template_name = 'experiments/experiments_create.html'



class ExperimentsUpdate(generic.UpdateView):
    model = Experiments
    fields = ['name', 'english_name', 'natural_range', 'physiopathology', 'reasons_for', 'change', 'interpretation', 'quick_interpretation', 'differential_diagnoses', 'false_results', 'references', 'gallery']
    template_name = 'experiments/experiments_update.html'

class ExperimentsDelete(generic.DeleteView):
    model = Experiments
    template_name = 'experiments/experiments_delete.html'
    success_url = reverse_lazy('experiments_list')


