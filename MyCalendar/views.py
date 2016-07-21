from django.views.generic import edit

from .models import Event, Task, Project, ProjectTask, UserProfile
from .forms import EventCreateForm, TaskCreateForm, ProjectCreateForm, ProjectTaskCreateForm
#from django.contrib.auth.models import User
from .models import Event, Task, Project, ProjectTask
from .forms import EventCreateForm, TaskCreateForm, ProjectCreateForm, ProjectTaskCreateForm
from django.contrib.auth.models import User


from .models import Event, Task, Project, ProjectTask
from .forms import  EventCreateForm, TaskCreateForm, ProjectCreateForm, ProjectTaskCreateForm
from django.contrib.auth.models import User

from django.shortcuts import render, redirect, get_object_or_404
from django.utils.safestring import mark_safe
from calendar import HTMLCalendar
from datetime import date, datetime, timedelta
from django.utils.timezone import now
from django.utils.html import conditional_escape as esc
from calendar import monthrange
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import Http404, HttpResponseRedirect



@login_required
def homeView(request):
    user = request.user
    user_tasks = Task.objects.filter(user__exact=user).order_by('task_date')
    user_projects = Project.objects.filter(user__exact=user).order_by('project_date')
    user_project_tasks = ProjectTask.objects.all().order_by('project_task_date')

    overdue_tasks = []
    overdue_projects = []
    overdue_project_tasks = []

    for task in user_tasks:
        if task.task_date < date.today():
            overdue_tasks.append(task)

    for project in user_projects:
        if project.project_date < date.today():
            overdue_projects.append(project)

    for project_task in user_project_tasks:
         if project_task.project_task_date < date.today():
                overdue_project_tasks.append(project_task)

    total_overdue = len(overdue_tasks) + len(overdue_projects) + len(overdue_project_tasks)

    return render(request, 'MyCalendar/home.html', {'total_overdue': total_overdue})


@login_required
def eventCreateView(request):
    profile = request.user.userprofile
    if request.method == "POST":
        form = EventCreateForm(data=request.POST)
        if form.is_valid():
            if form.cleaned_data['end_date'] < form.cleaned_data['start_date']:
                end_date = form.cleaned_data['end_date']
                start_date = form.cleaned_data['start_date']
                form = EventCreateForm()

                return render(request, 'MyCalendar/EventCreate.html',
                              {'form': form, 'end_date': end_date, 'start_date': start_date, 'profile': profile})

            elif form.cleaned_data['end_date'] == form.cleaned_data['start_date'] \
                    and form.cleaned_data['end_time'] < form.cleaned_data['start_time']:
                end_date = form.cleaned_data['end_date']
                start_date = form.cleaned_data['start_date']
                end_time = form.cleaned_data['end_time']
                start_time = form.cleaned_data['start_time']
                form = EventCreateForm()

                return render(request, 'MyCalendar/EventCreate.html',
                              {'form': form, 'end_time': end_time, 'start_time': start_time,
                               'end_date': end_date, 'start_date': start_date, 'profile': profile})

            event_without_user = form.save(commit=False)
            event_without_user.user = request.user
            form.save()

            return redirect('MyCalendar:calendar')

    else:
        form = EventCreateForm()
    return render(request, 'MyCalendar/EventCreate.html', {'form': form, 'profile': profile})



@method_decorator(login_required, name='dispatch')
class eventUpdateView(edit.UpdateView):
    model = Event
    form_class = EventCreateForm
    success_url = "/MyCalendar/"
    template_name_suffix = '_update_form'

    def get(self, request, pk, **kwargs):
        if request.user != self.get_object().user:
            raise Http404('Event does not exist.')
        else:
            return self.post(self, request)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(eventUpdateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['profile'] = self.request.user.userprofile

        return context


@method_decorator(login_required, name='dispatch')
class eventDeleteView(edit.DeleteView):
    model = Event
    template_name_suffix = '_delete'
    success_url = reverse_lazy('MyCalendar:calendar')


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(eventDeleteView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['profile'] = self.request.user.userprofile

        return context


@login_required
def taskListView(request):
    user = request.user
    user_tasks = Task.objects.filter(user__exact=user).order_by('task_date')
    user_projects = Project.objects.filter(user__exact=user).order_by('project_date')
    profile = user.userprofile

    overdue_tasks = []
    current_tasks = []
    overdue_projects = []
    current_projects = []

    for task in user_tasks:
        if task.task_date >= date.today():
            current_tasks.append(task)
        else:
            overdue_tasks.append(task)

    for project in user_projects:
        if project.project_date >= date.today():
            current_projects.append(project)
        else:
            overdue_projects.append(project)

    date_today = date.today()
    number_of_current_tasks = len(current_tasks)
    number_of_overdue_tasks = len(overdue_tasks)
    number_of_current_projects = len(current_projects)
    number_of_overdue_projects = len(overdue_projects)

    #to get the number of overdue project tasks
    user_project_tasks = ProjectTask.objects.all().order_by('project_task_date')
    overdue_project_tasks = []
    for project_task in user_project_tasks:
        if project_task.project_task_date < date.today():
            overdue_project_tasks.append(project_task)
    number_of_overdue_project_tasks = len(overdue_project_tasks)

    context = {'current_tasks': current_tasks,
               'number_of_current_tasks': number_of_current_tasks,
               'overdue_tasks': overdue_tasks,
               'number_of_overdue_tasks': number_of_overdue_tasks,
               'date_today': date_today,
               'current_projects': current_projects,
               'number_of_current_projects': number_of_current_projects,
               'overdue_projects': overdue_projects,
               'number_of_overdue_projects': number_of_overdue_projects,
               'profile': profile,
               'number_of_overdue_project_tasks': number_of_overdue_project_tasks
               }

    return render(request, 'MyCalendar/TasksView.html', context)



@login_required
def taskCreateView(request):
    profile = request.user.userprofile
    if request.method == "POST":
        form = TaskCreateForm(data=request.POST)
        if form.is_valid():
            task_without_user = form.save(commit=False)
            task_without_user.user = request.user
            form.save()

            return redirect('MyCalendar:tasklist')

    else:
        form = TaskCreateForm()

    return render(request, 'MyCalendar/TaskCreate.html', {'form': form, 'profile': profile})


@method_decorator(login_required, name='dispatch')
class taskUpdateView(edit.UpdateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("MyCalendar:tasklist")
    template_name = 'MyCalendar/TaskUpdate.html'


    def get(self, request, pk, **kwargs):
        if request.user != self.get_object().user:
            raise Http404('Task does not exist.')
        else:
            return self.post(self, request)


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(taskUpdateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['profile'] = self.request.user.userprofile

        return context


@method_decorator(login_required, name='dispatch')
class taskDeleteView(edit.DeleteView):
    model = Task
    template_name = 'MyCalendar/TaskDelete.html'
    success_url = reverse_lazy('MyCalendar:tasklist')


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(taskDeleteView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['profile'] = self.request.user.userprofile

        return context

@login_required
def taskCompleteView(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = True
    task.save()
    return redirect('MyCalendar:tasklist')






@login_required
def projectCreateView(request):
    profile = request.user.userprofile
    if request.method == "POST":
        form = ProjectCreateForm(data=request.POST)
        if form.is_valid():
            project_without_user = form.save(commit=False)
            project_without_user.user = request.user
            form.save()

            return redirect('MyCalendar:tasklist')

    else:
        form = ProjectCreateForm()

    return render(request, 'MyCalendar/ProjectCreate.html', {'form': form, 'profile': profile})

@method_decorator(login_required, name='dispatch')
class projectUpdateView(edit.UpdateView):
    model = Project
    form_class = ProjectCreateForm
    success_url = reverse_lazy("MyCalendar:tasklist")
    template_name = 'MyCalendar/ProjectUpdate.html'


    def get(self, request, pk, **kwargs):
        if request.user != self.get_object().user:
            raise Http404('Project does not exist.')
        else:
            return self.post(self, request)

@login_required
def projectTaskListView(request, project_id):
    profile = request.user.userprofile
    current_project = Project.objects.get(pk=project_id)
    project_tasks = ProjectTask.objects.filter(project=current_project).order_by('project_task_date')

    overdue_project_tasks = []
    current_project_tasks = []

    if request.user != current_project.user:
        raise Http404('Project does not exist.')

    for task in project_tasks:
        if task.project_task_date >= date.today():
            current_project_tasks.append(task)
        else:
            overdue_project_tasks.append(task)

    date_today = date.today()
    number_of_current_tasks = len(current_project_tasks)
    number_of_overdue_tasks = len(overdue_project_tasks)

    context = {'current_project_tasks': current_project_tasks,
               'number_of_current_tasks': number_of_current_tasks,
               'overdue_project_tasks': overdue_project_tasks,
               'number_of_overdue_tasks': number_of_overdue_tasks,
               'date_today': date_today,
               'project_id': project_id,
               'profile': profile
               }

    return render(request, 'MyCalendar/ProjectTasksView.html', context)


@method_decorator(login_required, name='dispatch')
class projectDeleteView(edit.DeleteView):
    model = Project
    template_name = 'MyCalendar/ProjectDelete.html'
    success_url = reverse_lazy('MyCalendar:tasklist')


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(projectDeleteView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['profile'] = self.request.user.userprofile

        return context


@login_required
def projectTaskCreateView(request, project_id):
    profile = request.user.userprofile
    current_project = Project.objects.get(pk=project_id)

    if request.method == "POST":
        form = ProjectTaskCreateForm(data=request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = current_project
            form.save()

            return redirect('MyCalendar:project_tasklist', project_id)

    else:
        form = ProjectTaskCreateForm()

    return render(request, 'MyCalendar/ProjectTaskCreate.html', {'form': form, 'profile': profile})


@method_decorator(login_required, name='dispatch')
class projectTaskUpdateView(edit.UpdateView):
    model = ProjectTask
    form_class = ProjectTaskCreateForm
    template_name = 'MyCalendar/ProjectTaskUpdate.html'


    def get(self, request, pk, **kwargs):
        if request.user != self.get_object().project.user:
            raise Http404('Project Task does not exist.')
        else:
            return self.post(self, request)


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(projectTaskUpdateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['project_id'] = self.get_object().project.pk
        context['profile'] = self.request.user.userprofile

        return context


@method_decorator(login_required, name='dispatch')
class projectTaskDeleteView(edit.DeleteView):
    model = ProjectTask
    template_name = 'MyCalendar/ProjectTaskDelete.html'

    def get_success_url(self):
        return reverse('MyCalendar:project_tasklist', kwargs={'project_id': self.object.project.pk})

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(projectTaskDeleteView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['project_id'] = self.get_object().project.pk
        context['profile'] = self.request.user.userprofile
        return context




class EventCalendar(HTMLCalendar):

    def __init__(self, events):
        super(EventCalendar, self).__init__()
        self.events = self.group_by_range(events)

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += ' today'
            if self.events != {} and self.year in self.events and self.month in self.events[self.year] \
                    and day in self.events[self.year][self.month]:
                cssclass += ' filled'
                body = ['<ul>']
                for event in self.events[self.year][self.month][day]:
                    body.append('<ol>')
                    body.append('<a href="%s" style="color:white; font-size:small">' % event.get_absolute_url())
                    body.append(esc(event.event_name))
                    body.append('</a>')
                    body.append('</ol>')
                body.append('</ul>')
                return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))
            return self.day_cell(cssclass, day)
        return self.day_cell('noday', '&nbsp;')

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(EventCalendar, self).formatmonth(year, month)


#experimental solution: creating a dictionary of dictionaries
    def group_by_range(self, events):
        end_dict = {}
        for event in events:
            start = event.start_date
            end = event.end_date
            event_range = [start]
            while start != end:
                start += timedelta(days=1)
                event_range.append(start)

            for event_date in event_range:
                if event_date.year in end_dict:
                    if event_date.month in end_dict[event_date.year]:
                        if event_date.day in end_dict[event_date.year][event_date.month]:
                            end_dict[event_date.year][event_date.month][event_date.day].append(event)
                        else:
                            end_dict[event_date.year][event_date.month][event_date.day] = [event]
                    else:
                        end_dict[event_date.year][event_date.month] = {event_date.day: [event]}
                else:
                    end_dict[event_date.year] = {event_date.month: {event_date.day: [event]}}

        return end_dict



    def day_cell(self, cssclass, body):
        return '<td class="%s">%s</td>' % (cssclass, body)

def named_month(pMonthNumber):
    """
    Return the name of the month, given the month number
    """
    return date(1900, pMonthNumber, 1).strftime('%B')

def home(request):
    """
    Show calendar of events this month
    """
    lToday = datetime.now()
    return calendarView(request, lToday.year, lToday.month)

@login_required
def calendarView(request, year=None, month=None):
    """
    Show calendar of events for specified month and year
    """
    if request.user.is_authenticated():
        profile = request.user.userprofile
        username = request.user.username
    else:
        return redirect('MyCalendar:login')

    if year == None and month == None:
        year = now().year
        month = now().month

    lYear = int(year)
    lMonth = int(month)
    lCalendarFromMonth = datetime(lYear, lMonth, 1)
    lCalendarToMonth = datetime(lYear, lMonth, monthrange(lYear, lMonth)[1])
    # for spanning events to work across months and/or years, the filter must only filter using username, which may be
    # redundant anyway. The above 2 variables are thus not in use.
    UserEvents = Event.objects.filter(user__username__exact=username)

    lCalendar = EventCalendar(UserEvents).formatmonth(lYear, lMonth)

    lPreviousYear = lYear
    lPreviousMonth = lMonth - 1
    if lPreviousMonth == 0:
        lPreviousMonth = 12
        lPreviousYear = lYear - 1
    lNextYear = lYear
    lNextMonth = lMonth + 1
    if lNextMonth == 13:
        lNextMonth = 1
        lNextYear = lYear + 1
    lYearAfterThis = lYear + 1
    lYearBeforeThis = lYear - 1

    return render(request, 'MyCalendar/cal_month.html', {'Calendar': mark_safe(lCalendar),
                                                         'Month' : lMonth,
                                                         'MonthName' : named_month(lMonth),
                                                         'Year' : lYear,
                                                         'PreviousMonth' : lPreviousMonth,
                                                         'PreviousMonthName' : named_month(lPreviousMonth),
                                                         'PreviousYear' : lPreviousYear,
                                                         'NextMonth' : lNextMonth,
                                                         'NextMonthName' : named_month(lNextMonth),
                                                         'NextYear' : lNextYear,
                                                         'YearBeforeThis' : lYearBeforeThis,
                                                         'YearAfterThis' : lYearAfterThis,
                                                         'username': username,
                                                         'profile': profile
                                                         })

