from django.shortcuts import render

# Create your views here.

# Get - Home
def home(request):
  return render(request, 'home.html')

# Get - About
def about(request):
  return render(request, 'about.html')

# USER STUFF
# sign up page
def signup(request):
  return render(request, 'user/signup.html')

# log in page
def login(request):
  return render(request, 'user/login.html')