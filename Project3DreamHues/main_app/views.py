from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from . models import Dream, DreamForm

import requests
import json

# Create your views here.

# Get - Home
def home(request):
  return render(request, 'home.html')

# Get - About
def about(request):
  return render(request, 'about.html')

# Get - dreams_index
def dreams_index(request):
    dreams = Dream.objects.all()
    # for dream in dreams: #TODO <--- shouldn't this be in the html to render all dreams there?
      # print(dream)
    return render(request, 'dreams/index.html', {'dreams': dreams} )

#GET - Detail
def dreams_detail(request, dream_id):
  dream = Dream.objects.get(id=dream_id)
  #TODO Add detail code if needed & code the detail HTML file
  return render(request, 'dreams/detail.html', { 'dream': dream})

# - CreateView, for dream form
class DreamCreate(CreateView):
  model = Dream
  fields = '__all__'

# - UpdateView
class DreamUpdate(UpdateView):
  model = Dream
  fields = ['name', 'about', 'feeling', 'dream_type']

# -DeleteView
class DreamDelete(DeleteView):
  model = Dream
  success_url = '/dreams'

# Get - random palette
def get_random_palette():
    url = 'http://colormind.io/api/'
    payload = {"model": "default"}
    response = requests.post(url, data=json.dumps(payload))
    if response.status_code == 200:
        return response.json()['result']
    else:
        return None

# USER STUFF
# sign up page
def custom_signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid sign up - try again'
    else:
        form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# log in page
def custom_login(request):
  return render(request, 'registration/login.html')