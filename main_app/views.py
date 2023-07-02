from typing import Any
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Crystal
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView


#---------------Routes----------------------#

class Home(TemplateView):
    template_name = "home.html"
    
class About(TemplateView):
    template_name = "about.html"

class CrystalList(TemplateView):
    template_name = "crystal_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None:
            context['crystals'] = Crystal.objects.filter(name__icontains=name)
            context['header'] = 'Searching for {name}'
        else:
            context['crystals'] = Crystal.objects.all()
            context['header'] = 'Crystal Collection'
        return context

class CrystalCreate(CreateView):
    model = Crystal
    fields = ['name', 'img', 'bio', 'location']
    template_name = 'crystal_create.html'
    success_url = '/crystals/'

class CrystalDetail(DetailView):
    model = Crystal
    template_name = 'crystal_detail.html'

class CrystalUpdate(UpdateView):
    model = Crystal
    fields = ['name', 'img', 'bio', 'location']
    template_name = 'crystal_update.html'
    success_url = '/crystals/'

class CrystalDelete(DeleteView):
    model = Crystal
    template_name = 'crystal_delete_confirmation.html'
    success_url = '/crystals/'