from django.contrib import admin
from django.urls import path, include
from core.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('activities/', include('activities.urls')),
    path('schedules/', include('schedules.urls')),
    path('', include('core.urls')),
    path('accounts/', include('accounts.urls')),
]
