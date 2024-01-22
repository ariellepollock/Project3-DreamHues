from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name="home"),
  path('about/', views.about, name='about'),

  # USER THINGS
  # signup page
  path('signup/', views.signup, name='signup'),
  # accounts
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/signup/', views.signup, name='signup'),
]