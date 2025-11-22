from django import forms
from .models import Activity_Schedule
from django.forms import inlineformset_factory

class ActivityScheduleForm(forms.ModelForm):
    class Meta:
        model = Activity_Schedule
        fields = ['activity', 'location', 'date', 'start_time', 'end_time', 'expected_participants',]
