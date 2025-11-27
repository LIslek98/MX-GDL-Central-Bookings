from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Activity_Schedule
from .forms import ActivityForm, Activity_ScheduleForm

def activity_list(request):
    scheds = Activity_Schedule.objects.all()
    context = {
        'activities': scheds
    }
    return render(request, 'activitylist.html', context)

@login_required
def create_activity(request):    
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('activity/list')
    else:
        form = ActivityForm()

    return render(request, 'create_activity_form.html', {
        'form': form
    })

@login_required
def create_activity_schedule(request):
    if request.method == 'POST':
        form = Activity_ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save()
            return redirect('activity/list', organizer_name=schedule.organizer.name)               # THIS IS JUST A PLACEHOLDER.
    else:
        form = Activity_ScheduleForm()

    return render(request, 'create_schedule_form.html', {
        'form': form
    })
