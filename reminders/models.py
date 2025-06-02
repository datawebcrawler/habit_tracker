# reminders/models.py
from django.db import models

# Create your models here.
import uuid
from django.db import models
from django.conf import settings

class Reminder(models.Model):
    STATUS_CHOICES = [('pendente', 'Pendente'), ('feito', 'Feito'), ('abortado', 'Abortado')]
    RECURRENCE_CHOICES = [('unico', 'Único'), ('diario', 'Diário'), ('semanal', 'Semanal'), ('mensal', 'Mensal')]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    schedule_date = models.DateField()
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')
    recurrence = models.CharField(max_length=10, choices=RECURRENCE_CHOICES, default='unico')