from django.urls import path
from . import views

urlpatterns = [
    path('activity/list/', views.activity_list, name='activitylist'),
    path('activity/create/', views.create_activity, name='createactivity'),
    path('activity/schedule/create', views.create_activity_schedule, name='createactivityschedule'),
]