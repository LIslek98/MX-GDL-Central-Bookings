from django.urls import path
from . import views

urlpatterns = [
    path('activity/list/', views.activity_list, name='activitylist'),
    path('activity/create/', views.activity_create, name='activitycreate'),
]