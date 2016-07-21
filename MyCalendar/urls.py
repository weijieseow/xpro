from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

app_name = 'MyCalendar'

urlpatterns = [
    # /MyCalendar/
    url(r'^$', views.calendarView, name='calendar'),

    # /MyCalendar/home
    url(r'^home/$', views.homeView, name='home'),

    # /MyCalendar/calendar
    url(r'^calendar/([0-9]{4})/([0-9]+)/$', views.calendarView, name='calendar'),

    # /MyCalendar/event/#pk
    url(r'^event/(?P<pk>[0-9]+)/$', views.eventUpdateView.as_view(), name="eventupdate"),

    # /MyCalendar/event/delete
    url(r'^event/(?P<pk>[0-9]+)/delete/$', views.eventDeleteView.as_view(), name="eventdelete"),

    # logout
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),

    # /MyCalendar/EventCreate
    url(r'^EventCreate/$', views.eventCreateView, name='eventcreate'),

    # /MyCalendar/TaskList
    url(r'^TaskList/$', views.taskListView, name='tasklist'),

    # /MyCalendar/TaskList/completed/
    url(r'^TaskList/completed/$', views.completedView, name="completed"),

    # /MyCalendar/TaskList/TaskCreate
    url(r'^TaskList/TaskCreate/$', views.taskCreateView, name='taskcreate'),

    # /MyCalendar/TaskList/task/#pk
    url(r'^TaskList/task/(?P<pk>[0-9]+)/$', views.taskUpdateView.as_view(), name="taskupdate"),

    # /MyCalendar/TaskList/task/#pk/delete
    url(r'^TaskList/task/(?P<pk>[0-9]+)/delete/$', views.taskDeleteView.as_view(), name="taskdelete"),

    # /MyCalendar/TaskList/task/#pk/complete
    url(r'^TaskList/task/(?P<pk>[0-9]+)/complete/$', views.taskCompleteView, name="taskcomplete"),

    # /MyCalendar/TaskList/task/#pk/uncomplete
    url(r'^TaskList/task/(?P<pk>[0-9]+)/uncomplete/$', views.taskUncompleteView, name="taskuncomplete"),

    # /MyCalendar/TaskList/ProjectCreate
    url(r'^TaskList/ProjectCreate/$', views.projectCreateView, name='projectcreate'),

    # /MyCalendar/TaskList/project/#pk/update
    url(r'^TaskList/project/(?P<pk>[0-9]+)/update/$', views.projectUpdateView.as_view(), name="projectupdate"),

    # /MyCalendar/TaskList/project/#pk/delete
    url(r'^TaskList/project/(?P<pk>[0-9]+)/delete/$', views.projectDeleteView.as_view(), name="projectdelete"),

    # /MyCalendar/TaskList/project/#pk/complete
    url(r'^TaskList/project/(?P<pk>[0-9]+)/complete/$', views.projectCompleteView, name="projectcomplete"),

    # /MyCalendar/TaskList/project/#pk/uncomplete
    url(r'^TaskList/project/(?P<pk>[0-9]+)/uncomplete/$', views.projectUncompleteView, name="projectuncomplete"),

    # /MyCalendar/TaskList/project/#pk
    url(r'^TaskList/project/(?P<project_id>[0-9]+)/$', views.projectTaskListView, name="project_tasklist"),

    # /MyCalendar/TaskList/project/ProjectTaskCreate
    url(r'^TaskList/project/(?P<project_id>[0-9]+)/ProjectTaskCreate/$', views.projectTaskCreateView, name='project_taskcreate'),

    # /MyCalendar/TaskList/project/ptask/#pk/update
    url(r'^TaskList/project/(?P<project_id>[0-9]+)/(?P<pk>[0-9]+)/update/$', views.projectTaskUpdateView.as_view(), name="project_taskupdate"),

    # /MyCalendar/TaskList/project/ptask/#pk/delete
    url(r'^TaskList/project/(?P<project_id>[0-9]+)/(?P<pk>[0-9]+)/delete/$', views.projectTaskDeleteView.as_view(), name="project_taskdelete"),

    # /MyCalendar/TaskList/project/ptask/#pk/complete
    url(r'^TaskList/project/(?P<project_id>[0-9]+)/(?P<pk>[0-9]+)/complete/$', views.projectTaskCompleteView, name="project_taskcomplete"),

    # /MyCalendar/TaskList/project/ptask/#pk/uncomplete
    url(r'^TaskList/project/(?P<project_id>[0-9]+)/(?P<pk>[0-9]+)/uncomplete/$', views.projectTaskUncompleteView, name="project_taskuncomplete"),

    ]