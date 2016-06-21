from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'MyCalendar'

urlpatterns = [
    # /MyCalendar/
    url(r'^$', views.calendarView, name='calendar'),

    # /MyCalendar/event/#pk
    #url(r'^event/(?P<event_id>[0-9]+)/$', views.EventView.as_view(), name="event"),

    # /MyCalendar/task/#pk
    # url(r'^task/(?P<task_id>[0-9]+)/$', views,TaskView.as_view(), name="task"),

    # /MyCalendar/AboutUs
    url(r'^AboutUs/$', views.aboutUsView, name="aboutus"),

    # /MyCalendar/register
    url(r'^register/$', views.registerView, name='register'),

    # /MyCalendar/login
    url(r'^login/$', views.loginView, name='login'),
]