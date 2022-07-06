from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Sup

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def sups_index(request):
    sups = Sup.objects.all()
    return render(request, 'sups/index.html', {'sups': sups})

def sups_detail(request, sup_id):
  sup = Sup.objects.get(id=sup_id)
  return render(request, 'sups/detail.html', { 'sup': sup })

class SupCreate(CreateView):
  model = Sup
  fields = '__all__'
  success_url = '/supplements/'

class SupUpdate(UpdateView):
  model = Sup
  fields = ['dosage', 'description', 'amt']

class SupDelete(DeleteView):
  model = Sup
  success_url = '/supplements/'

