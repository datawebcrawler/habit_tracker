# activities/models.py
import uuid
from django.db import models
from django.conf import settings

class Activity(models.Model):
    FREQUENCY_CHOICES = [('unica', 'Única'), ('diaria', 'Diária'), ('semanal', 'Semanal'), ('mensal', 'Mensal')]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column='user_id'
    )
    activity = models.TextField()
    category = models.TextField(blank=True, null=True)
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, default='unica')

    class Meta:
        db_table = 'activities'

    def __str__(self):
        return self.activity