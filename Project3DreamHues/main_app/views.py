from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
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
    dreams = Dream.objects.filter()
    for dream in dreams: #TODO <--- shouldn't this be in the html to render all dreams there?
      print(dream)
    return render(request,  {'dreams': dreams}, 'dreams/index.html' )

#GET - Detail
def dreams_detail(request):
   #TODO Add detail code if needed & code the detail HTML file
   return render(request, 'dreams/detail.html')

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
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

# log in page
def login(request):
  return render(request, 'registration/login.html')