# core/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy

# Modelos
from activities.models import Activity
from datetime import date

@login_required
def home(request):
    context = {}

    if request.user.is_authenticated:
        today = date.today()

        # Atividades diárias (do app Activities)
        daily_activities = Activity.objects.filter(
            user=request.user,
            frequency='diaria'
        )

        # Contexto final
        context.update({
            'daily_activities': daily_activities,
            'today': today.strftime("%d/%m/%Y"),
            'username': request.user.get_full_name() or request.user.username or request.user.email
        })

    return render(request, 'core/home.html', context)