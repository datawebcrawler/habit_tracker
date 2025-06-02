# schedules/forms.py
from django import forms
from schedules.models import Schedule
from activities.models import Activity

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['activity', 'scheduled_date', 'start_time', 'status']
        widgets = {
            'scheduled_date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'})
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            # Filtra apenas as atividades do usuário logado
            self.fields['activity'].queryset = Activity.objects.filter(user=user)