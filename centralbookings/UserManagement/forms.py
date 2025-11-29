from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Organizer, Participant, Contact_Person

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Organizer, Participant, Contact_Person

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ParticipantForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            }
        )
    )
    class Meta:
        model = Participant
        fields = [
            'first_name', 'middle_name', 'last_name', 
            'birth_date', 'participant_type', 'department'
            ]

class OrganizerForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = [
            'name', 'organizer_type', 'street',
            'barangay', 'city', 'region'
            ]

class ContactPersonForm(forms.ModelForm):
    class Meta:
        model = Contact_Person
        fields = [
            'first_name', 'middle_name', 'last_name', 
            'contact_email', 'contact_number'
            ]
