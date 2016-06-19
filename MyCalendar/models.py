from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now

class Event(models.Model):
    event_name = models.CharField(max_length = 255)
    # we may need to come up with a way to do choices for date and time
    from_date_and_time = models.DateTimeField(verbose_name= 'Start', default= now())
    to_date_and_time = models.DateTimeField(verbose_name='End', help_text= 'Please set end time to later than start time.')
    description = models.TextField()


    # recurrence?

    def __str__(self):
        return self.event_name

