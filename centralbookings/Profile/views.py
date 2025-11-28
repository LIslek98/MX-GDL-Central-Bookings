from django.shortcuts import render, get_object_or_404, redirect
from .models import Organizer, Participant 

def profile_Organizer_View(request, organizer_id):
    organizer = get_object_or_404(Organizer, pk=organizer_id)
    return render(request, 'profile/organizer_profile.html', {'organizer': organizer})



def profile_Participant_View(request, participant_id):
    participant = get_object_or_404(Participant, pk=participant_id)
    return render(request, 'profile/participant_profile.html', {'participant': participant})
