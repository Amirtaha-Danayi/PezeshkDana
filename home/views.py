from django.shortcuts import render
from django.views import generic

class ShowHome(generic.TemplateView):
    template_name = 'home.html'

