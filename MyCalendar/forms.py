from django.contrib.auth.models import User
from .models import UserProfile, Event, Task
from django import forms
from.custom_widgets import SelectTimeWidget

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=("Username"), error_messages={ 'invalid': ("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=("Email address"))
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        exclude = ['first_name', 'last_name']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['bio']


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'start_date', 'start_time', 'end_date', 'end_time', 'description']
        widgets = {'start_date': forms.SelectDateWidget, 'start_time': SelectTimeWidget,
                   'end_date': forms.SelectDateWidget, 'end_time': SelectTimeWidget, 'class':'form-control',
                   'description': forms.Textarea(attrs={'rows': 1, 'cols': 40, 'style': 'height: 3em;'})}


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'task_date', 'description']
        widgets = {'task_date': forms.SelectDateWidget, 'description': forms.Textarea(attrs={'rows': 1, 'cols': 40, 'style': 'height: 3em;'})}
