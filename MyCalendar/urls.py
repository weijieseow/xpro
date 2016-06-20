from django.conf.urls import url
from . import views

app_name = 'MyCalendar'

urlpatterns = [
    # /calendar/
    url(r'^$', views.calendarView, name='calendar'),

    # /calendar/event/#pk
    #url(r'^event/(?P<event_id>[0-9]+)/$', views.EventView.as_view(), name="event"),

    # /calendar/task/#pk
    # url(r'^task/(?P<task_id>[0-9]+)/$', views,TaskView.as_view(), name="task"),

    # /calendar/aboutus
    url(r'^AboutUs/$', views.aboutUsView, name="aboutus"),
]