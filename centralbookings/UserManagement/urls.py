from django.urls import path
from .views import UserListView, ParticipantRegisterView, OrganizerRegisterView

urlpatterns = [
    path('register', UserListView.as_view(), name='register'),
    path('register/participant', ParticipantRegisterView.as_view(), name='register-participant'),
    path('register/organizer', OrganizerRegisterView.as_view(), name='register-organizer'),
]

app_name = "UserManagement"
