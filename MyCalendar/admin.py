from django.contrib import admin

from .models import Event, UserProfile, Task

admin.site.register(Event)
admin.site.register(UserProfile)
admin.site.register(Task)