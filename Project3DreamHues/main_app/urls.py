from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('dreams/', views.dreams_index, name='index'),

  # USER THINGS
  # signup page
  path('signup/', views.signup, name='signup'),
  # log in page
  path('login/', views.login, name='login'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)