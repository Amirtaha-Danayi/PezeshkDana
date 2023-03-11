from django.shortcuts import render
from django.views import generic
from .models import Sickness
from django.urls import reverse_lazy
from .forms import SicknessForm



class SicknessList(generic.ListView):
    model = Sickness
    template_name = 'sickness/sickness_list.html'
    context_object_name = 'sickness'


class SicknessDetail(generic.DetailView):
    model = Sickness
    template_name = 'sickness/sickness_detail.html'


def create_sickness(request):

    form = None
    if request.method == "POST":
        form = SicknessForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'sickness/sickness_list.html')
    else:

        form = SicknessForm()
    return render(request, 'sickness/sickness_create.html',{'form':form})



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