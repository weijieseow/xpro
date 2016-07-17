from __future__ import unicode_literals
from django.db.models.signals import post_save
from django.db import models
from datetime import date, timedelta
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=30, default='Set a Display Name here!')

    def __str__(self):
        return self.display_name


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

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


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255)
    project_date = models.DateField(null=True, default=date.today())
    description = models.TextField(blank=True)

    def __str__(self):
        return self.project_name

    def get_absolute_url(self):
        return "/MyCalendar/TaskList/project/%i/" % self.pk


class ProjectTask(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    project_task_name = models.CharField(max_length=255)
    project_task_date = models.DateField(null=True, default=date.today())
    description = models.TextField(blank=True)

    def __str__(self):
        return self.project_task_name

    def get_absolute_url(self):
        return "/MyCalendar/TaskList/project/%i/" % self.project.pk



