from django.contrib.auth.models import User
from .models import UserProfile, Event
from django import forms
from.custom_widgets import SelectTimeWidget

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        exclude = ('first_name', 'last_name')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('bio',)


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_name', 'start_date', 'start_time', 'end_date', 'end_time', 'description')
        widgets = {'start_date': forms.SelectDateWidget, 'start_time': SelectTimeWidget,
                   'end_date': forms.SelectDateWidget, 'end_time': SelectTimeWidget}


