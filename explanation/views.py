from django.shortcuts import render
from django.views import generic
from .models import Explanation
from django.urls import reverse_lazy
from .forms import ExplanationForm
from django.http import HttpResponseRedirect


class ExplanationList(generic.ListView):
    model = Explanation
    template_name = 'explanation/explanation_list.html'
    context_object_name = 'explanation'


class ExplanationDetail(generic.DetailView):
    model = Explanation
    template_name = 'explanation/explanation_detail.html'


def create_explanation(request):

    form = None
    if request.method == "POST":
        form = ExplanationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:

        form = ExplanationForm()
    return render(request, 'explanation/explanation_create.html',{'form':form})







class ExplanationUpdate(generic.UpdateView):
    model = Explanation
    fields = '__all__'
    template_name = 'explanation/explanation_update.html'

class ExplanationDelete(generic.DeleteView):
    model = Explanation
    template_name = 'explanation/explanation_delete.html'
    success_url = reverse_lazy('explanation_list')