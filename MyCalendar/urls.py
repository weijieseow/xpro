from django.conf.urls import url
from . import views

from django.contrib.auth import views as auth_views

app_name = 'MyCalendar'

urlpatterns = [
    # /MyCalendar/
    url(r'^$', views.calendarView, name='calendar'),

    # /MyCalendar/calendar
    url(r'^calendar/([0-9]{4})/([0-9]+)/$', views.calendarView, name='calendar'),

    # /MyCalendar/event/#pk
    url(r'^event/(?P<pk>[0-9]+)/$', views.eventUpdateView.as_view(), name="eventupdate"),

    # /MyCalendar/event/delete
    url(r'^event/(?P<pk>[0-9]+)/delete/$', views.eventDeleteView.as_view(), name="eventdelete"),

    # /MyCalendar/register
    #url(r'^register/$', views.registerView, name='register'),

    # /MyCalendar/login
    #url(r'^login/$', views.loginView, name='login'),

    # logout
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),

    # /MyCalendar/EventCreate
    url(r'^EventCreate/$', views.eventCreateView, name='eventcreate'),

    # /MyCalendar/TaskList
    url(r'^TaskList/$', views.taskListView, name='tasklist'),

    # /MyCalendar/TaskCreate
    url(r'^TaskCreate/$', views.taskCreateView, name='taskcreate'),

    # /MyCalendar/task/#pk
    url(r'^task/(?P<pk>[0-9]+)/$', views.taskUpdateView.as_view(), name="taskupdate"),

    # /MyCalendar/task/#pk/delete
    url(r'^task/(?P<pk>[0-9]+)/delete/$', views.taskDeleteView.as_view(), name="taskdelete"),

]