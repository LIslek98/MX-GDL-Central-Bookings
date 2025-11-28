from django.urls import path
from .views import ActivityListView, ActivityTypeCreateView, ActivityScheduleCreateView, ActivityParticipantsList

urlpatterns = [
    path('activity/', ActivityListView.as_view(), name='activity-list'),
    path('activity/details/<int:id>', ActivityParticipantsList, name='details'),
    path('activity/book', ActivityListView.as_view(), name='activity-book'),
    path('activity/create/', ActivityTypeCreateView.as_view(), name='create-activity'),
    path('activity/schedule/create/', ActivityScheduleCreateView.as_view(), name='createa-ctivity-schedule'),
]

app_name = "main"