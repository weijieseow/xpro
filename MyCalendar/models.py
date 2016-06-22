from __future__ import unicode_literals

from django.db import models
from datetime import date, timedelta
from django.contrib.auth.models import User

'''
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    bio= models.TextField(blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.user.username
'''

class Event(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    event_name = models.CharField(max_length = 255)
    start_date = models.DateField(null=True, default=date.today())
    start_time = models.TimeField(null=True)
    end_date = models.DateField(null=True, default=date.today() + timedelta(minutes=30))
    end_time = models.TimeField(null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.event_name

    #find out how to get this working
    #def get_absolute_url(self):
    #    return ('event', (), {'event_id': self.pk})
