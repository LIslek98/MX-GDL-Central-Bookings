from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Profile.models import Activity_Schedule

def activity_list(request):
    scheds = Activity_Schedule.objects.all()
    context = {
        'activities': scheds
    }
    return render(request, 'activitylist.html', context)

def activity_create(request):
    scheds = Activity_Schedule.objects.all()
    context = {
        'activities': scheds
    }
    return render(request, 'activitylist.html', context)