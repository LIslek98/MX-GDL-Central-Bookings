from django.shortcuts import render, get_object_or_404, redirect
from .models import Organizer, Participant 
from .forms import Activity_ScheduleForm, ActivityForm

def profile_Organizer_View(request, organizer_name):
    organizer = get_object_or_404(Organizer, name=organizer_name)
    context = {
        'organizer': organizer
    }
    return render(request, 'profile/organizer_profile.html', context)


def profile_Participant_View(request, participant_name):
    participant = get_object_or_404(Participant, name=participant_name)
    context = {
        'participant': participant
    }
    return render(request, 'profile/participant_profile.html', context)

def create_schedule(request):
    if request.method == 'POST':
        form = Activity_ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save()
            return redirect('Profile:profile_Organizer_View', organizer_name=schedule.organizer.name)               # THIS IS JUST A PLACEHOLDER.
    return render(request, 'profile/schedule_form.html', {
        'form': form
    })

def create_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile/organizer_profile.html')                                                       # THIS IS ALSO A PLACEHOLDER.
    return render(request, 'profile/schedule_form.html', {
        'form': form
    })
