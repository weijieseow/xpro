
from .models import Event, Task, Project, ProjectTask, UserProfile
from django.contrib.auth.models import User
from django import forms
#from.custom_widgets import SelectTimeWidget
from functools import partial


DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


class ChangeEmailForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(max_length=30)), label="Email address", required=False)

    class Meta:
        model = User
        fields = ['email']


class ChangeDisplayNameForm(forms.ModelForm):
    display_name = forms.CharField(required=False)

    class Meta:
        model = UserProfile
        fields = ['display_name']


class EventCreateForm(forms.ModelForm):

    start_date = forms.DateField(widget=DateInput())
    start_time = forms.TimeField(widget=TimeInput(format='%H:%M'))
    end_date = forms.DateField(widget=DateInput())
    end_time = forms.TimeField(widget=TimeInput(format='%H:%M'))

    class Meta:
        model = Event
        fields = ['event_name', 'start_date', 'start_time', 'end_date', 'end_time', 'description']
        widgets = {'description': forms.Textarea(attrs={'rows': 1, 'cols': 40, 'style': 'height: 3em;'})}


class TaskCreateForm(forms.ModelForm):

    task_date = forms.DateField(widget=DateInput())

    class Meta:
        model = Task
        fields = ['task_name', 'task_date', 'description']
        widgets = {'description': forms.Textarea(attrs={'rows': 1, 'cols': 40, 'style': 'height: 3em;'})}


class ProjectCreateForm(forms.ModelForm):

    project_date = forms.DateField(widget=DateInput())

    class Meta:
        model = Project
        fields = ['project_name', 'project_date', 'description']
        widgets = {'description': forms.Textarea(attrs={'rows': 1, 'cols': 40, 'style': 'height: 3em;'})}


class ProjectTaskCreateForm(forms.ModelForm):

    project_task_date = forms.DateField(widget=DateInput())

    class Meta:
        model = ProjectTask
        fields = ['project_task_name', 'project_task_date', 'description']
        widgets = {'description': forms.Textarea(attrs={'rows': 1, 'cols': 40, 'style': 'height: 3em;'})}


