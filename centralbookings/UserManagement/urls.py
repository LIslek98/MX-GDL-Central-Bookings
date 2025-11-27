from django.urls import path
from .views import UserCreateView, ParticipantCreateView, OrganizerCreateView

urlpatterns = [
    path('register', UserCreateView.as_view(), name='register'),
    path('register/participant', ParticipantCreateView.as_view(), name='register'),
    path('register/organizer', OrganizerCreateView.as_view(), name='register'),
]

app_name = "UserManagement"
