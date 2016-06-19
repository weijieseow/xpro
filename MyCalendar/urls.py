from django.conf.urls import patterns, url
from .views import #

app_name = 'MyCalendar'

urlpatterns = [
    # /calender/
    url(r'^$', CalendarView.as_view(), name='calendar'),

    # /calendar/event/#pk
    url(r'^event/(?P<event_id>[0-9]+)/$', EventView.as_view(), name="event"),

    # /calendar/task/#pk
    url(r'^task/(?P<task_id>[0-9]+)/$', TaskView.as_view(), name="task")
]