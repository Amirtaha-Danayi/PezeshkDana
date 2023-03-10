from django.shortcuts import render
from django.views import generic
from .models import Medicines
from django.urls import reverse_lazy


class MedicinesList(generic.ListView):
    model = Medicines
    template_name = 'medicines/medicines_list.html'
    context_object_name = 'medicines'


class MedicinesDetail(generic.DetailView):
    model = Medicines
    template_name = 'medicines/medicines_detail.html'


class MedicinesCreate(generic.CreateView):
    model = Medicines
    fields = ['title', 'english_title', 'generic_name', 'english_name', 'pronunciation', 'synonyms', 'other_names', 'brands', 'main_drug_category', 'summary', 'mechanism_of_action', 'indications', 'contraindications', 'related_treatments', 'related_conditions', 'drug_dose', 'different_dosage_forms', 'drug_interactions', 'food_interactions', 'drug_absorption', 'half_life', 'toxicity', 'method_of_consumption', 'adverse_effects', 'side_effects', 'symptoms_of_excessive_consumption', 'warnings', 'gallery', 'references']
    template_name = 'medicines/medicines_create.html'


class MedicinesUpdate(generic.UpdateView):
    model = Medicines
    fields = ['title', 'english_title', 'generic_name', 'english_name', 'pronunciation', 'synonyms', 'other_names', 'brands', 'main_drug_category', 'summary', 'mechanism_of_action', 'indications', 'contraindications', 'related_treatments', 'related_conditions', 'drug_dose', 'different_dosage_forms', 'drug_interactions', 'food_interactions', 'drug_absorption', 'half_life', 'toxicity', 'method_of_consumption', 'adverse_effects', 'side_effects', 'symptoms_of_excessive_consumption', 'warnings', 'gallery', 'references']
    template_name = 'medicines/medicines_update.html'

class MedicinesDelete(generic.DeleteView):
        model = Medicines
        template_name = 'medicines/medicines_delete.html'
        success_url = reverse_lazy('medicines_list')
