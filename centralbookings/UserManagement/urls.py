from django.urls import path
from .views import HomepageView, ParticipantRegisterView, OrganizerRegisterView

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('register/participant', ParticipantRegisterView.as_view(), name='register-participant'),
    path('register/organizer', OrganizerRegisterView.as_view(), name='register-organizer'),
]

app_name = "UserManagement"
