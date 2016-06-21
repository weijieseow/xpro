from django.views import generic
from .models import Event
from .forms import UserForm, UserProfileForm
from django.shortcuts import render
from django.utils.safestring import mark_safe
from calendar import HTMLCalendar
from datetime import date, datetime
from itertools import groupby
from django.utils.timezone import now
from django.utils.html import conditional_escape as esc
from calendar import monthrange
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

#class EventView(generic.ListView):
#    template_name = 'MyCalendar/Event.html'

def aboutUsView(request):
    return render(request, 'MyCalendar/AboutUs.html')

class EventCalendar(HTMLCalendar):

    def __init__(self, events):
        super(EventCalendar, self).__init__()
        self.events = self.group_by_day(events)

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += ' today'
            if day in self.events:
                cssclass += ' filled'
                body = ['<ul>']
                for event in self.events[day]:
                    body.append('<li>')
                    #body.append('<a href="%s">' % event.get_absolute_url())
                    body.append(esc(event.event_name))
                    body.append('</li>')
                body.append('</ul>')
                return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))
            return self.day_cell(cssclass, day)
        return self.day_cell('noday', '&nbsp;')

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(EventCalendar, self).formatmonth(year, month)

    def group_by_day(self, events):
        field = lambda event: event.start_date.day
        return dict(
            [(day, list(items)) for day, items in groupby(events, field)]
        )

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
    return calendar(request, lToday.year, lToday.month)

def calendarView(request, year=now().year, month=now().month):
    """
    Show calendar of events for specified month and year
    """
    lYear = int(year)
    lMonth = int(month)
    lCalendarFromMonth = datetime(lYear, lMonth, 1)
    lCalendarToMonth = datetime(lYear, lMonth, monthrange(lYear, lMonth)[1])
    MonthlyEvents = Event.objects.filter(start_date__gte=lCalendarFromMonth, start_date__lte=lCalendarToMonth)
    lCalendar = EventCalendar(MonthlyEvents).formatmonth(lYear, lMonth)
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

    return render(request, 'MyCalendar/cal_month.html', {'Calendar' : mark_safe(lCalendar),
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
                                                   })

def registerView(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of UserForm
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        
        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(
            request, 'MyCalendar/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def loginView(request):
    # Like before, obtain the context for the user's request.

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/MyCalendar/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your X-Pro account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'MyCalendar/login.html')