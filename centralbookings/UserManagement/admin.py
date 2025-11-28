from django.contrib import admin
from .models import Organizer, Participant, Activity, Contact_Person, Room, Location, Activity_Schedule, Department, Activity_Booking

admin.site.register(Contact_Person)
admin.site.register(Organizer)
admin.site.register(Location)
admin.site.register(Activity)
admin.site.register(Activity_Schedule)
admin.site.register(Department)
admin.site.register(Participant)
admin.site.register(Activity_Booking)