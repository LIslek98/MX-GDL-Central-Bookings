from django.urls import path
from .views import ActivityListView, ActivityTypeCreateView, ActivityScheduleUpdateView, ActivityScheduleCreateView, ActivityParticipantsListView, BookActivityView

urlpatterns = [
    path('activity/', ActivityListView.as_view(), name='activity-list'),
    path('activity/details/<int:id>', ActivityParticipantsListView.as_view(), name='details'),
    path('activity/edit/<int:schedule_id>', ActivityScheduleUpdateView.as_view(), name='edit-activity'),
    path('activity/book', ActivityListView.as_view(), name='activity-book'),
    path('book/<int:schedule_id>/', BookActivityView.as_view(), name='book_schedule'),
    path('activity/create/', ActivityTypeCreateView.as_view(), name='create-activity'),
    path('activity/schedule/create/', ActivityScheduleCreateView.as_view(), name='create-activity-schedule'),
]

app_name = "main"