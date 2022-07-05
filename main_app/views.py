from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class Sup:
  def __init__(self, name, dosage, description, amt):
    self.name = name
    self.dosage = dosage
    self.description = description
    self.amt = amt

sups = [
  Sup('Vitamin C', '1000 mg', 'Antioxidant Protection', 1),
  Sup('Ubiquinol', '100 mg', 'Cardiovascular Health', 1),
  Sup('Alpha Lipoic Acid', '600 mg', 'Energy Production', 2)
]

def sup_index(request):
    return render(request, 'sups/index.html', {'sups': sups})