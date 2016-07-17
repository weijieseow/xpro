from django.contrib.auth.views import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from MyCalendar.forms import ChangeEmailForm, ChangeDisplayNameForm


def custom_login(request, **kwargs):
    if request.user.is_authenticated():
        return redirect('MyCalendar:home')
    else:
        return login(request, **kwargs)


def index_view(request):
    if request.user.is_authenticated():
        return redirect('MyCalendar:home')
    else:
        return render(request, 'index.html')



@login_required
def change_email(request):
    user = request.user
    profile = user.userprofile
    if request.method == 'POST':
        form = ChangeEmailForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('MyCalendar:tasklist')
        else:
            print(form.errors)
    else:
        form = ChangeEmailForm(instance=user)
    return render(
        request, 'registration/change_email.html',
        {'form': form, 'profile': profile})

@login_required
def change_display_name(request):
    user = request.user
    profile = user.userprofile
    if request.method == 'POST':
        form = ChangeDisplayNameForm(data=request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('MyCalendar:tasklist')
        else:
            print(form.errors)
    else:
        form = ChangeDisplayNameForm(instance=profile)
    return render(
        request, 'registration/change_display_name.html',
        {'form': form, 'profile': profile})



