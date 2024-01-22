from django.shortcuts import render

from . models import Dream
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

    for dream in dreams:
      print(dream)
    return render(request, 'dreams/index.html', {
        'dreams': dreams
    })

# USER STUFF
# sign up page
def signup(request):
  return render(request, 'user/signup.html')

# log in page
def login(request):
  return render(request, 'user/login.html')