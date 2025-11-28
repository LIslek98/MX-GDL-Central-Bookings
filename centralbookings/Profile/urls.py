"""Direct users to appropriate urls depending on needs."""
from django.urls import path
from .views import profile_Organizer_View, profile_Participant_View

app_name = "Profile"

urlpatterns = [
    path('profile/organizer/<int:organizer_id>/', profile_Organizer_View, name='profile_Organizer_View'),
    path('profile/participant/<int:participant_id>/', profile_Participant_View, name="profile_Participant_View"),
]