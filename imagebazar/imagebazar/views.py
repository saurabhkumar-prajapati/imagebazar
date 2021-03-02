from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
class ShowAboutPage(TemplateView):
    template_name ='about.html'






