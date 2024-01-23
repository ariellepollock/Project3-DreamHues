from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('dreams/', views.dreams_index, name='index'),
  path('dreams/<int:dream_id>', views.dreams_detail, name='detail'),
  # USER THINGS
  # log in page
  path('login/', views.login, name='login'),
  # log out
  path('logout/', LogoutView.as_view(), name='logout'),
  # accounts
  path('accounts/', include('django.contrib.auth.urls')),
  # signup page
  path('accounts/signup/', views.signup, name='signup'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_URL)

