from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Organizer, Participant

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'birth_date', 'participant_type', 'department']
        
class OrganizerForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = ['name', 'organizer_type', 'contact_person']
        