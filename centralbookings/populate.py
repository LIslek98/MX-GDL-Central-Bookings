import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'centralbookings.settings')
django.setup()

from django.contrib.auth.models import User
from UserManagement.models import Contact_Person, Organizer, Building, Location, Activity, Activity_Schedule, Department, Participant, Activity_Booking

# Clear old data (optional, useful if testing multiple times)
Contact_Person.objects.all().delete()
Organizer.objects.all().delete()
Building.objects.all().delete()
Location.objects.all().delete()
Activity.objects.all().delete()
Activity_Schedule.objects.all().delete()
Department.objects.all().delete()
Participant.objects.all().delete()
Activity_Booking.objects.all().delete()

# ------------------
# Contact Persons
# ------------------
cp1 = Contact_Person.objects.create(contact_person_id=10001, first_name='Juan', middle_name='Santos', last_name='Dela Cruz',
                                   contact_email='juan@example.com', contact_number='091-712-345')
cp2 = Contact_Person.objects.create(contact_person_id=10002, first_name='Maria', middle_name='Reyes', last_name='Lopez',
                                   contact_email='maria@example.com', contact_number='091-812-345')
cp3 = Contact_Person.objects.create(contact_person_id=10003, first_name='Jose', middle_name='Garcia', last_name='Tan',
                                   contact_email='jose@example.com', contact_number='091-912-345')
cp4 = Contact_Person.objects.create(contact_person_id=10004, first_name='Ana', middle_name='Cruz', last_name='Santos',
                                   contact_email='ana@example.com', contact_number='092-012-345')
cp5 = Contact_Person.objects.create(contact_person_id=10005, first_name='Luis', middle_name='Martinez', last_name='De la Vega',
                                   contact_email='luis@example.com', contact_number='092-112-345')

# ------------------
# Users
# ------------------
u1 = User.objects.create_user(username='org1', password='password123')
u2 = User.objects.create_user(username='org2', password='password123')
u3 = User.objects.create_user(username='p1', password='password123')
u4 = User.objects.create_user(username='p2', password='password123')
u5 = User.objects.create_user(username='p3', password='password123')

# ------------------
# Organizers
# ------------------
org1 = Organizer.objects.create(user=u1, organizer_id=10001, name='The Computer Society of the Ateneo', organizer_type='INTERNAL', contact_person=cp1,
                                street='Katipunan Ave', barangay='Loyola Heights', city='Quezon City', region='NCR')
org2 = Organizer.objects.create(user=u2, organizer_id=10002, name='Ateneo Athletics', organizer_type='INTERNAL', contact_person=cp2,
                                street='Katipunan Ave', barangay='Loyola Heights', city='Quezon City', region='NCR')

# ------------------
# Buildings
# ------------------
b1 = Building.objects.create(building_id=10001, building_name='Faber Hall')
b2 = Building.objects.create(building_id=10002, building_name='Gonzaga Hall')

# ------------------
# Locations
# ------------------
loc1 = Location.objects.create(location_id=10001, building=b1, room_name='Room 101', max_capacity=30)
loc2 = Location.objects.create(location_id=10002, building=b2, room_name='Room 202', max_capacity=50)

# ------------------
# Activities
# ------------------
act1 = Activity.objects.create(activity_id=10001, activity_name='Coding Workshop')
act2 = Activity.objects.create(activity_id=10002, activity_name='Math Lecture')

# ------------------
# Activity Schedule
# ------------------
sched1 = Activity_Schedule.objects.create(schedule_ID=10001, date='2025-12-01', start_time='09:00:00', end_time='11:00:00',
                                          expected_participants=25, organizer=org1, location=loc1, activity=act1)
sched2 = Activity_Schedule.objects.create(schedule_ID=10002, date='2025-12-02', start_time='13:00:00', end_time='15:00:00',
                                          expected_participants=40, organizer=org2, location=loc2, activity=act2)

# ------------------
# Departments
# ------------------
dep1 = Department.objects.create(department_ID=10001, department_name='Computer Science')
dep2 = Department.objects.create(department_ID=10002, department_name='Mathematics')

# ------------------
# Participants
# ------------------
p1 = Participant.objects.create(user=u3, participant_ID=10001, first_name='Alice', middle_name='May', last_name='Reyes',
                                birth_date='2002-05-12', participant_type='ST', department=dep1)
p2 = Participant.objects.create(user=u4, participant_ID=10002, first_name='Bob', middle_name='Lao', last_name='Tan',
                                birth_date='1998-11-03', participant_type='FM', department=dep2)
p3 = Participant.objects.create(user=u5, participant_ID=10003, first_name='Charlie', middle_name='Pascual', last_name='Santos',
                                birth_date='2001-07-22', participant_type='ST', department=dep1)

# ------------------
# Activity Bookings
# ------------------
Activity_Booking.objects.create(booking_ID=10001, schedule=sched1, participant=p1, has_attended=True)
Activity_Booking.objects.create(booking_ID=10002, schedule=sched1, participant=p3, has_attended=False)
Activity_Booking.objects.create(booking_ID=10003, schedule=sched2, participant=p2, has_attended=True)

print("Database populated successfully!")
