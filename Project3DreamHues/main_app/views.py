import os
from typing import Any
import uuid
import boto3

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from . models import Dream, DreamForm, Photo

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
@login_required
def dreams_index(request):
  dreams = Dream.objects.filter(owner=request.user)
  # print(dream)
  return render(request, 'dreams/index.html', {'dreams': dreams} )

#GET - Detail
def dreams_detail(request, dream_id):
  dream = Dream.objects.get(id=dream_id)
  return render(request, 'dreams/detail.html', { 'dream': dream})

# - CreateView, for dream form

class DreamCreate(CreateView):
  model = Dream
  form_class = DreamForm
  # template_name = 'dream_form.html'

  def form_valid(self, form):
    form.instance.owner = self.request.user
    return super().form_valid(form)
  
  def get_form_kwargs(self):
    kwargs = super().get_form_kwargs()
    kwargs['user'] = self.request.user
    return kwargs

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

# add_photo
def add_photo(request, dream_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]

    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
      Photo.objects.create(url=url, dream_id=dream_id)

    except Exception as e:
      print('woah nelly! an error occurred uploading your file')
      print(e)

  return redirect('detail', dream_id=dream_id)

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