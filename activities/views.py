# activities/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from activities.models import Activity
from activities.forms import ActivityForm

@login_required
def activity_list(request):
    activities = Activity.objects.filter(user=request.user)
    return render(request, 'activities/activity_list.html', {'activities': activities})

@login_required
def activity_create(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.user = request.user
            activity.save()
            messages.success(request, 'Atividade criada com sucesso!')
            return redirect('activities:activity_list')

    else:
        form = ActivityForm()

    return render(request, 'activities/activity_form.html', {'form': form})

# activities/views.py
@login_required
def activity_update(request, pk):  # Agora aceita str
    activity = get_object_or_404(Activity, id=pk, user=request.user)
    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            messages.success(request, 'Atividade atualizada com sucesso!')
            return redirect('activities:activity_list')
    else:
        form = ActivityForm(instance=activity)

    return render(request, 'activities/activity_form.html', {'form': form, 'activity': activity})

@login_required
def activity_delete(request, pk):  # Também usa str
    activity = get_object_or_404(Activity, id=pk, user=request.user)
    activity.delete()
    messages.success(request, 'Atividade excluída com sucesso!')
    return redirect('activities:activity_list')


@login_required
def activity_check_in(request, pk):  # Também usa str
    from datetime import date
    activity = get_object_or_404(Activity, id=pk, user=request.user)
    activity.last_checked = date.today()
    activity.save()
    messages.success(request, f'{activity.activity} marcado como feito hoje!')
    return redirect('activities:activity_list')