from django.contrib.auth.views import login

from django.shortcuts import render, redirect



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