from django import forms
from UserManagement.models import Activity, Activity_Schedule, Organizer
from django.forms import inlineformset_factory

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['activity_name']
        exclude = ['organizer']
        
class Activity_ScheduleForm(forms.ModelForm):

    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            }
        )
    )

    start_time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                'type': 'time',
                'class': 'form-control'
            }
        )
    )

    end_time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                'type': 'time',
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = Activity_Schedule
        fields = [
            'activity',
            'location',
            'date',
            'start_time',
            'end_time',
        ]


class ActivityFilterForm(forms.Form):

    organizer = forms.ModelChoiceField(
        queryset = Organizer.objects.all(),
        empty_label = "All Organizers",
        required = False
    )

    date = forms.DateField(
        required = False,
        widget=forms.DateInput(
        attrs={'type': 'date', 'autocomplete': 'off',
               'class': 'form-control'}))
    
    