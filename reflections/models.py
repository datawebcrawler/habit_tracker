# reflections/models.py
from django.db import models

# Create your models here.
import uuid
from django.db import models
from django.conf import settings

class Reflection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    learned = models.TextField(blank=True, null=True)
    improved = models.TextField(blank=True, null=True)
    failed = models.TextField(blank=True, null=True)
    feeling = models.IntegerField(null=True, blank=True)