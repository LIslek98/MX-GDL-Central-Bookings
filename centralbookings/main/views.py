from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from UserManagement.models import Activity_Schedule, Activity, Activity_Booking
from .forms import ActivityForm, Activity_ScheduleForm, ActivityFilterForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.utils import timezone

class ActivityListView(ListView):
    model = Activity_Schedule
    context_object_name = "schedules"

    def get_template_names(self):
        path = self.request.path

        if path.endswith("book") or path.endswith("book/"):
                return "activity_book.html"

        return "activity_list.html"
    
    def get_queryset(self):  
        queryset = super().get_queryset()  
        filter_form = ActivityFilterForm(self.request.GET)  
    
        if filter_form.is_valid():  
            activity_type = filter_form.cleaned_data.get("activity_type")
            organizer =  filter_form.cleaned_data.get("organizer")
            date =  filter_form.cleaned_data.get("date")
    
            if activity_type:  
                queryset = queryset.filter(activity=activity_type) 

            if organizer:
                 queryset = queryset.filter(organizer=organizer) 

            if date:
                 queryset = queryset.filter(date=date) 
    
        return queryset

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['filter_form'] = ActivityFilterForm(self.request.GET)

        return ctx
    
def ActivityParticipantsList(request, id):
    sched = Activity_Schedule.objects.get(schedule_ID=id)
    bookings = Activity_Booking.objects.all()
    context = {
        'sched': sched,
        'bookings': bookings,
    }

    return render(request, 'activity_details.html', context)


    
class ActivityTypeCreateView(CreateView):
    model = Activity
    template_name = "activity_type_add.html"
    form_class = ActivityForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("main:activity-list")

class ActivityScheduleCreateView(CreateView):
    model = Activity_Schedule
    template_name = "activity_schedule_add.html"
    form_class = Activity_ScheduleForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("main:activity-list")

# @login_required
def book_activity(request, schedule_id):
    participant = request.user.participant
    schedule = get_object_or_404(Activity_Schedule, schedule_ID=schedule_id)
    booking, created = Activity_Booking.objects.get_or_create( #temp solution; ideally should check if booking exists first and if it does the option is unbook maybe
        participant=participant,
        schedule=schedule,
        defaults={'has_attended': False, 'booking_date': timezone.now().date()}
    )