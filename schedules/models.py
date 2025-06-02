# schedules/models.py
import uuid
from django.db import models
from activities.models import Activity

class Schedule(models.Model):
    STATUS_CHOICES = [('pendente', 'Pendente'), ('feito', 'Feito'), ('adiado', 'Adiado')]

    id = models.CharField(
        max_length=36,
        primary_key=True,
        default=str(uuid.uuid4),
        editable=False
    )
    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        db_column='activity_id'
    )
    scheduled_date = models.DateField(db_column='scheduled_date')
    start_time = models.TimeField()  # ← Nova sugestão!
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pendente'
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'schedule'

    def __str__(self):
        return f"{self.scheduled_date} - {self.start_time}: {self.activity}"