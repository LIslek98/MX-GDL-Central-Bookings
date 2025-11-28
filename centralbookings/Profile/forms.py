"""Create forms with appropriate fields."""

from django import forms
from .models import Activity_Schedule, Activity, Location


class Activity_ScheduleForm(forms.ModelForm):
    """Create a form to add details for the Activity Schedule"""

    class Meta:
        """Create fields for the form and link Article model."""

        model = Activity_Schedule
        fields = ['date', 'start_time', 'end_time', 'expected_participants', 'organizer', 'location', 'activity']           #note that we only want the admin to create the locations. I assume this is just a dropdown window of all the existing locations.


class ActivityForm(forms.ModelForm):
    """Creates a form to add activity_name"""

    class Meta:
        """Create fields for the form and link ArticleImage model."""

        model = Activity
        fields = ['activity_name']
