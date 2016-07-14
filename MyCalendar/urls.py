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

    # logout
    url(r'^logout/$', auth_views.logout_then_login, name='logout'),

    # /MyCalendar/EventCreate
    url(r'^EventCreate/$', views.eventCreateView, name='eventcreate'),

    # /MyCalendar/TaskList
    url(r'^TaskList/$', views.taskListView, name='tasklist'),

    # /MyCalendar/TaskCreate
    url(r'^TaskList/TaskCreate/$', views.taskCreateView, name='taskcreate'),

    # /MyCalendar/task/#pk
    url(r'^TaskList/task/(?P<pk>[0-9]+)/$', views.taskUpdateView.as_view(), name="taskupdate"),

    # /MyCalendar/task/#pk/delete
    url(r'^TaskList/task/(?P<pk>[0-9]+)/delete/$', views.taskDeleteView.as_view(), name="taskdelete"),

    # /MyCalendar/ProjectCreate
    url(r'^TaskList/ProjectCreate/$', views.projectCreateView, name='projectcreate'),

    # /MyCalendar/project/#pk/delete
    url(r'^TaskList/project/(?P<pk>[0-9]+)/delete/$', views.projectDeleteView.as_view(), name="projectdelete"),

    # /MyCalendar/project#pk
    url(r'^TaskList/project/(?P<project_id>[0-9]+)/$', views.projectTaskListView, name="project_tasklist"),

    # /MyCalendar/project/ProjectTaskCreate
    url(r'^TaskList/project/(?P<project_id>[0-9]+)/ProjectTaskCreate/$', views.projectTaskCreateView, name='project_taskcreate'),

    # /MyCalendar/project/ptask/#pk/update
    url(r'^TaskList/project/(?P<project_id>[0-9]+)/(?P<pk>[0-9]+)/update/$', views.projectTaskUpdateView.as_view(), name="project_taskupdate"),

    # /MyCalendar/project/ptask/#pk/delete
    url(r'^TaskList/project/(?P<proj>[0-9]+)/(?P<pk>[0-9]+)/delete/$', views.projectTaskDeleteView.as_view(), name="project_taskdelete"),
]