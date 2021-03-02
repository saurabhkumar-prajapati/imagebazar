

# Create your views here.
from django.shortcuts import render,redirect
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from myapp.models import *
class ShowAboutPage(TemplateView):
    template_name ='about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Learnwithme'
        context['link'] = 'https://www.google.coobjecm'
        return context

class ShowHomePage(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Image.objects.all()
        context['categories']=Category.objects.all()

        return context

    template_name = 'home.html'

class ShowCategoryPage(TemplateView,):

    def get_context_data(self,cid, **kwargs,):
        context = super().get_context_data(**kwargs)
        context['images'] = Image.objects.filter(cat=cid)
        context['categories']=Category.objects.all()
        context['category']=Category.objects.get(pk=cid)


        return context

    template_name = 'home.html'

class ShowHome(TemplateView,):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Image.objects.all()
        context['categories']=Category.objects.all()

        return context


def search(request):
    if request.method == "GET":
        search= request.GET.get('search')
        titlesearch=Image.objects.all().filter(title=search)
        return render(request,'search.html',{"titlesearch":titlesearch})


