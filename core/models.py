from django.db import models
from activities.models import Activity
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class DailyActivity(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.activity.name} - {self.date}"
    