from django.contrib.auth.models import User
from .models import UserProfile, Event
from django import forms

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=("Username"), error_messages={ 'invalid': ("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=("Email address"))
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        exclude = ('first_name', 'last_name')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio',)

class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_name', 'start_date', 'start_time', 'end_date', 'end_time', 'description')

