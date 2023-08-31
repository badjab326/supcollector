from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Sup, Type, Taking
from .forms import TakingForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def sups_index(request):
    sups = Sup.objects.filter(user=request.user)
    return render(request, 'sups/index.html', {'sups': sups})

@login_required
def sups_detail(request, sup_id):
  sup = Sup.objects.get(id=sup_id)
  taking_form = TakingForm()
  types_sup_doesnt_have = Type.objects.filter(user=request.user).exclude(id__in = sup.types.all().values_list('id'))
  return render(request, 'sups/detail.html', {
    'sup': sup, 'taking_form': taking_form,
    'types': types_sup_doesnt_have
  })

@login_required
def types_index(request):
  types = Type.objects.filter(user=request.user)
  return render(request, 'types/index.html', {'types': types})

@login_required
def add_taking(request, sup_id):
  # create the ModelForm using the data in request.POST
  form = TakingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_taking = form.save(commit=False)
    new_taking.sup_id = sup_id
    new_taking.save()
  return redirect('detail', sup_id=sup_id)

@login_required
def assoc_type(request, sup_id, type_id):
  Sup.objects.get(id=sup_id).types.add(type_id)
  return redirect('detail', sup_id=sup_id)

@login_required
def assoc_type_delete(request, sup_id, type_id):
  Sup.objects.get(id=sup_id).types.remove(type_id)
  return redirect('detail', sup_id=sup_id)

class SupCreate(LoginRequiredMixin, CreateView):
  model = Sup
  fields = ['name', 'dosage', 'description', 'amt']
  success_url = '/supplements/'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class SupUpdate(LoginRequiredMixin, UpdateView):
  model = Sup
  fields = ['dosage', 'description', 'amt']

class SupDelete(LoginRequiredMixin, DeleteView):
  model = Sup
  success_url = '/supplements/'

# class TypeList(LoginRequiredMixin, ListView):
#   model = Type
#   template_name = 'types/index.html'

class TypeDetail(LoginRequiredMixin, DetailView):
  model = Type
  template_name = 'types/detail.html'

class TypeCreate(LoginRequiredMixin, CreateView):
    model = Type
    fields = ['name', 'method']
    success_url = '/types/'
    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class TypeUpdate(LoginRequiredMixin, UpdateView):
    model = Type
    fields = ['name', 'method']

class TypeDelete(LoginRequiredMixin, DeleteView):
    model = Type
    success_url = '/types/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid info - please try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)