from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Activity_Schedule
from .forms import ActivityScheduleForm, ActivityForm, Activity_ScheduleForm

def activity_list(request):
    scheds = Activity_Schedule.objects.all()
    context = {
        'activities': scheds
    }
    return render(request, 'activitylist.html', context)

@login_required
def activity_create(request):
    form = ActivityScheduleForm()
    
    if request.method == 'POST':
        form = ActivityScheduleForm(request.POST)
       
        if form.is_valid():
            form.save()
            return redirect('activitylist')
    else:
        form = ActivityScheduleForm()

    return render(request, 'create_form.html', {'create_form': form})

def create_schedule(request):
    if request.method == 'POST':
        form = Activity_ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save()
            return redirect('Profile:profile_Organizer_View', organizer_name=schedule.organizer.name)               # THIS IS JUST A PLACEHOLDER.
    else:
        form = Activity_ScheduleForm()

    return render(request, 'profile/schedule_form.html', {
        'form': form
    })

def create_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile/organizer_profile.html')
    else:
        form = ActivityForm()

    return render(request, 'profile/schedule_form.html', {
        'form': form
    })
