from django import forms
from .models import Activity, Activity_Schedule
from django.forms import inlineformset_factory

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['activity_name']
        
class Activity_ScheduleForm(forms.ModelForm):
    class Meta:
        model = Activity_Schedule
        fields = ['activity', 'location', 'date', 'start_time', 'end_time', 'expected_participants', 'organizer']
