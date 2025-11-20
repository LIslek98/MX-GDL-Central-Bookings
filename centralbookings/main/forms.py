from django import forms
from .models import Activity_Schedule
from django.forms import inlineformset_factory

class ActivityScheduleForm(forms.ModelForm):
    class Meta:
        model = Activity_Schedule
        fields = ['title', 'description', 'status']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
        }