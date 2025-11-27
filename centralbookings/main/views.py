from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Activity_Schedule, Activity
from .forms import ActivityForm, Activity_ScheduleForm, ActivityFilterForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

class ActivityListView(ListView):
    model = Activity_Schedule
    template_name = "activity_list.html"
    context_object_name = "schedules"

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

  