import os
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Dog, DogWalker
from .forms import FeedingForm

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def dogs_index(request):
  dogs = Dog.objects.all()
  return render(request, 'dogs/index.html', {
    'dogs': dogs
  })

def dogs_detail(request, dog_id):
  dog = Dog.objects.get(id=dog_id)
  id_list = dog.dogwalker.all().values_list('id')
  no_dogwalker = DogWalker.objects.exclude(id__in=id_list)
  feeding_form = FeedingForm()
  return render(request, 'dogs/detail.html', { 'dog': dog, 'feeding_form': feeding_form, 'dogwalker': no_dogwalker })


class DogCreate(CreateView):
  model = Dog
  fields = ['name', 'breed', 'description', 'age']
  
class DogUpdate(UpdateView):
  model = Dog
  fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
  model = Dog
  success_url = '/dogs'

def add_feeding(request, dog_id):
    form = FeedingForm(request.POST)
  # validate the form
    if form.is_valid():
    # don't save the form to the db until it
    # has the dog_id assigned
      new_feeding = form.save(commit=False)
      new_feeding.dog_id = dog_id
      new_feeding.save()
    return redirect('detail', dog_id=dog_id)

class DogWalkerList(ListView):
  model = DogWalker

class DogWalkerDetail(DetailView):
  model = DogWalker

class DogWalkerCreate(CreateView):
  model = DogWalker
  fields = ['name']

class DogWalkerUpdate(UpdateView):
  model = DogWalker
  fields = ['name']

class DogWalkerDelete(DeleteView):
  model = DogWalker
  success_url = '/dogwalker'

def assoc_dogwalker(request, dog_id, dogwalker_id):
  Dog.objects.get(id=dog_id).dogwalker.add(dogwalker_id)
  return redirect('detail', dog_id=dog_id)

def unassoc_dogwalker(request, dog_id, dogwalker_id):
  Dog.objects.get(id=dog_id).dogwalker.remove(dogwalker_id)
  return redirect('detail', dog_id=dog_id)