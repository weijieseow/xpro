# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.9.7 on 2016-07-13 13:33
=======
# Generated by Django 1.9.7 on 2016-07-11 11:52
>>>>>>> tyean-ya-edit
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=255)),
<<<<<<< HEAD
                ('start_date', models.DateField(default=datetime.date(2016, 7, 13), null=True)),
                ('start_time', models.TimeField(null=True)),
                ('end_date', models.DateField(default=datetime.date(2016, 7, 13), help_text='The end date must be later than the start date', null=True)),
=======
                ('start_date', models.DateField(default=datetime.date(2016, 7, 11), null=True)),
                ('start_time', models.TimeField(null=True)),
                ('end_date', models.DateField(default=datetime.date(2016, 7, 11), help_text='The end date must be later than the start date', null=True)),
>>>>>>> tyean-ya-edit
                ('end_time', models.TimeField(help_text='The end must be later than the start ', null=True)),
                ('description', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255)),
                ('project_date', models.DateField(default=datetime.date(2016, 7, 13), null=True)),
                ('description', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_task_name', models.CharField(max_length=255)),
                ('project_task_date', models.DateField(default=datetime.date(2016, 7, 13), null=True)),
                ('description', models.TextField(blank=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyCalendar.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=255)),
<<<<<<< HEAD
                ('task_date', models.DateField(default=datetime.date(2016, 7, 13), null=True)),
=======
                ('task_date', models.DateField(default=datetime.date(2016, 7, 11), null=True)),
>>>>>>> tyean-ya-edit
                ('description', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True)),
                ('user', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
