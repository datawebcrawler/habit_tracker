from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from activities.models import Activity
from accounts.models import CustomUser
from schedules.models import Schedule
from reflections.models import Reflection
from reminders.models import Reminder

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Activity)
admin.site.register(Schedule)
admin.site.register(Reflection)
admin.site.register(Reminder)
