from __future__ import unicode_literals

from django.db import models
from datetime import date, timedelta
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, editable=False)
    display_name = models.CharField(max_length=255)


    def __str__(self):
        return self.display_name


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=255)
    start_date = models.DateField(null=True, default=date.today())
    start_time = models.TimeField(null=True)
    end_date = models.DateField(null=True, default=date.today(),
                                help_text='The end date must be later than the start date')
    end_time = models.TimeField(null=True, help_text='The end must be later than the start ')


    description = models.TextField(blank=True)


    def __str__(self):
        return self.event_name

    def get_absolute_url(self):
        return "/MyCalendar/event/%i/" % self.pk


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=255)
    task_date = models.DateField(null=True, default=date.today())
    description = models.TextField(blank=True)

    def __str__(self):
        return self.task_name

    def get_absolute_url(self):
        return "/MyCalendar/task/%i/" % self.pk

'''
class AGroup(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(Model)
    group_name = models.CharField(max_length=255)

    description = models.TextField(blank=True)


    def __str__(self):
        return self.group_name


class GroupTask(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(AGroup)
    task_name = models.CharField(max_length=255)
    task_date = models.DateField(null=True, default=date.today())
    description = models.TextField(blank=True)

    def __str__(self):
        return self.task_name
'''