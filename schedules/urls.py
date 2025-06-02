# schedules/urls.py
from django.urls import path
from . import views

app_name = 'schedules'

urlpatterns = [
    path('', views.schedule_list, name='schedule_list'),
    path('add/', views.schedule_create, name='schedule_create'),
    path('edit/<uuid:pk>/', views.schedule_update, name='schedule_update'),
    path('delete/<uuid:pk>/', views.schedule_delete, name='schedule_delete'),
    path('checkin/<uuid:pk>/', views.schedule_check_in, name='schedule_check_in'),
]