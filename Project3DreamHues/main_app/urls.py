from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name="home"),
  path('about/', views.about, name='about'),

  # USER THINGS
  # signup page
  path('signup/', views.signup, name='signup'),
  # log in page
  path('login/', views.login, name='login'),
]