from django.urls import path
from .views import ActivityListView, ActivityTypeCreateView, ActivityScheduleCreateView, ActivityParticipantsListView, BookActivityView

urlpatterns = [
    path('activity/', ActivityListView.as_view(), name='activity-list'),
    path('activity/details/<int:id>', ActivityParticipantsListView.as_view(), name='details'),
    path('activity/book', ActivityListView.as_view(), name='activity-book'),
    path('book/<int:schedule_id>/', BookActivityView.as_view(), name='book_schedule'),
    path('activity/create/', ActivityTypeCreateView.as_view(), name='create-activity'),
    path('activity/schedule/create/', ActivityScheduleCreateView.as_view(), name='create-activity-schedule'),
]

app_name = "main"