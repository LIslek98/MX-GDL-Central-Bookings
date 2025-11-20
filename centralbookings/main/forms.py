from django import forms
from .models import Activity_Schedule
from django.forms import inlineformset_factory

class ActivityScheduleForm(forms.ModelForm):
    class Meta:
        model = Activity_Schedule
        fields = ['Activity', 'Location', 'Date', 'Start_Time', 'End_Time', 'Expected_Participants',]
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
        }