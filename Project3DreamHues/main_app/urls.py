from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('dreams/', views.dreams_index, name='index'),
  path('dreams/<int:dream_id>', views.dreams_detail, name='detail'),
  path('dreams/create', views.DreamCreate.as_view(), name='dreams_create'),
  path('dreams/<int:pk>/update', views.DreamUpdate.as_view(), name='dreams_update'),
  path('dreams/<int:pk>/delete', views.DreamDelete.as_view(), name='dreams_delete'),
  # USER THINGS
  # log in page
  path('login/', views.login, name='login'),
  # accounts
  path('accounts/', include('django.contrib.auth.urls')),
  # signup page
  path('accounts/signup/', views.signup, name='signup'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_URL)

