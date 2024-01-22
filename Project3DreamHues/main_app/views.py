from django.shortcuts import render, requests

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
  return render(request, 'user/signup.html')

# log in page
def login(request):
  return render(request, 'user/login.html')