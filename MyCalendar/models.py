from __future__ import unicode_literals

from django.db import models
from datetime import date, timedelta

class Event(models.Model):
    event_name = models.CharField(max_length = 255)
    start_date = models.DateField(null=True, default=date.today())
    start_time = models.TimeField(null=True, default=date.today())
    end_date = models.DateField(null=True, default=date.today())
    end_time = models.TimeField(null=True, default=date.today() + timedelta(minutes=30))
    description = models.TextField(blank=True)


    def __self__(self):
        return self.event_name

    #find out how to get this working
    #def get_absolute_url(self):
    #    return ('event', (), {'event_id': self.pk})
