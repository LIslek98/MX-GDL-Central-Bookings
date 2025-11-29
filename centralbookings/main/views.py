from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from UserManagement.models import Activity_Schedule, Activity, Activity_Booking
from .forms import ActivityForm, Activity_ScheduleForm, ActivityFilterForm
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin

class ActivityListView(LoginRequiredMixin, ListView):
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
            organizer =  filter_form.cleaned_data.get("organizer")
            date =  filter_form.cleaned_data.get("date")
     

            if organizer:
                 queryset = queryset.filter(activity__organizer=organizer) 

            if date:
                 queryset = queryset.filter(date=date) 
    
        return queryset

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['filter_form'] = ActivityFilterForm(self.request.GET)

        return ctx

   
class ActivityParticipantsListView(LoginRequiredMixin, ListView):
    model = Activity_Booking
    template_name = 'activity_details.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        sched_id = self.kwargs['id']
        return Activity_Booking.objects.filter(schedule__schedule_ID=sched_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sched'] = Activity_Schedule.objects.get(schedule_ID=self.kwargs['id'])
        return context

    def post(self, request, *args, **kwargs):
        booking_ids = request.POST.getlist('attended') 
        
        all_bookings = Activity_Booking.objects.filter(schedule__schedule_ID=self.kwargs['id'])
        
        for booking in all_bookings:
            booking.has_attended = str(booking.booking_ID) in booking_ids
            booking.save()

        return redirect(request.path)

class ActivityTypeCreateView(LoginRequiredMixin, CreateView):
    model = Activity
    template_name = "activity_type_add.html"
    form_class = ActivityForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("main:activity-list")

class ActivityScheduleCreateView(LoginRequiredMixin, CreateView):
    model = Activity_Schedule
    template_name = "activity_schedule_add.html"
    form_class = Activity_ScheduleForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("main:activity-list")

class BookActivityView(LoginRequiredMixin, View):
    def post(self, request, schedule_id):
        participant = request.user.participant
        schedule = get_object_or_404(Activity_Schedule, schedule_ID=schedule_id)
        
        booking, created = Activity_Booking.objects.get_or_create( #temp solution; ideally should check if booking exists first and if it does the option is unbook maybe
            participant=participant,
            schedule=schedule,
            defaults={
                'has_attended': False,
                'booking_date': timezone.now().date()
            }
        )
        return redirect('main:activity-list')