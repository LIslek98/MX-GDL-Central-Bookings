"""Direct users to appropriate urls depending on needs."""
from django.urls import path
from .views import profile_Organizer_View, profile_Participant_View, create_schedule, create_activity

app_name = "Profile"

urlpatterns = [
    path('profile/Organizer/<str:organizer_name>/', profile_Organizer_View, name='profile_Organizer_View'),
    path('profile/Participant/<str:participant_name>/', profile_Participant_View, name="profile_Participant_View"),
]