from django.contrib.auth.views import login
from django.http import HttpResponseRedirect
from django.conf.urls import url


def custom_login(request, **kwargs):
    if request.user.is_authenticated():
        return HttpResponseRedirect(url('MyCalendar:TaskList'))
    else:
        return login(request, **kwargs)

