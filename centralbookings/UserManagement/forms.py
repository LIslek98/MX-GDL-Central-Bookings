from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Organizer, Participant, Contact_Person

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'
        exclude = ['user', 'participant_ID']

class OrganizerForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = '__all__'
        exclude = ['user', 'organizer_id', 'contact_person']


class ContactPersonForm(forms.ModelForm):
    class Meta:
        model = Contact_Person
        fields = '__all__'
        exclude = ['contact_person_id']
