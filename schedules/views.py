# schedules/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from schedules.models import Schedule
from schedules.forms import ScheduleForm

@login_required
def schedule_list(request):
    schedules = Schedule.objects.filter(activity__user=request.user)
    return render(request, 'schedules/list.html', {'schedules': schedules})

@login_required
def schedule_create(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST, user=request.user)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.save()
            messages.success(request, 'Agendamento criado com sucesso!')
            return redirect('schedules:schedule_list')
    else:
        form = ScheduleForm(user=request.user)

    return render(request, 'schedules/form.html', {'form': form})

@login_required
def schedule_update(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk, activity__user=request.user)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            messages.success(request, 'Agendamento atualizado com sucesso!')
            return redirect('schedules:schedule_list')
    else:
        form = ScheduleForm(instance=schedule)

    return render(request, 'schedules/form.html', {'form': form, 'schedule': schedule})

@login_required
def schedule_delete(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk, activity__user=request.user)
    schedule.delete()
    messages.success(request, 'Agendamento excluído com sucesso!')
    return redirect('schedules:schedule_list')

@login_required
def schedule_check_in(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk, activity__user=request.user)
    schedule.status = 'feito'
    schedule.save()
    messages.success(request, 'Agendamento marcado como concluído!')
    return redirect('schedules:schedule_list')