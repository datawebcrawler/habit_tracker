# activities/urls.py
from django.urls import path
from . import views

app_name = 'activities'

urlpatterns = [
    path('', views.activity_list, name='activity_list'),
    path('add/', views.activity_create, name='activity_create'),
    path('edit/<str:pk>/', views.activity_update, name='activity_update'),
    path('delete/<str:pk>/', views.activity_delete, name='activity_delete'),
    path('checkin/<str:pk>/', views.activity_check_in, name='activity_check_in'),
]