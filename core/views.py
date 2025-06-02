# core/views.py

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User  # ou seu CustomUser se estiver em outra app
from users.forms import CustomUserCreationForm

# Modelos
from activities.models import Activity
from datetime import date

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

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