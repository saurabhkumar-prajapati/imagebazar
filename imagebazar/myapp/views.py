

# Create your views here.
from django.db.models import Q
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

def story_detail(request,id): #testing for search bar
    story=get_object_or_404(Image,id=id)
    return render(request,'search.html',{'story':story})



def searchbar(request):

    results=[]
    if request.method=="GET":
        query=request.GET.get('search')
        results=Image.objects.filter(title=query)
    return  render(request,'search.html',{'query': query,
                                          'results': results})




class Search(ListView):
    template_name = "search.html"
    context_object_name = "posts"
    def get_queryset(self):
        query = self.request.GET.get('search')
        return Image.objects.filter(title=query) #.order_by('-created_at')




