from django.urls import path
from .views import ActivityListView, ActivityTypeCreateView, ActivityScheduleCreateView

urlpatterns = [
    path('activity/', ActivityListView.as_view(), name='activity-list'),
    path('activity/create/', ActivityTypeCreateView.as_view(), name='create-activity'),
    path('activity/schedule/create/', ActivityScheduleCreateView.as_view(), name='createa-ctivity-schedule'),
]

app_name = "main"