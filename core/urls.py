# urls.py

from django.contrib.auth import views as auth_views
from .views import home
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
]
