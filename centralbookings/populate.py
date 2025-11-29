import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'centralbookings.settings')
django.setup()

from django.contrib.auth.models import User
from UserManagement.models import Contact_Person, Organizer, Building, Location, Activity,Activity_Schedule, Department, Participant, Activity_Booking

Activity_Booking.objects.all().delete()
Participant.objects.all().delete()
Department.objects.all().delete()
Activity_Schedule.objects.all().delete()
Activity.objects.all().delete()
Location.objects.all().delete()
Building.objects.all().delete()
Organizer.objects.all().delete()
Contact_Person.objects.all().delete()
User.objects.all().delete()

# USERS
users = [
    # orgaanizers
    User.objects.create_user(username='org1', password='password123'),
    User.objects.create_user(username='org2', password='password123'),
    User.objects.create_user(username='org3', password='password123'),
    User.objects.create_user(username='org4', password='password123'),
    User.objects.create_user(username='org5', password='password123'),
    User.objects.create_user(username='org6', password='password123'),
    User.objects.create_user(username='org7', password='password123'),

    # participants
    User.objects.create_user(username='p1', password='password123'),
    User.objects.create_user(username='p2', password='password123'),
    User.objects.create_user(username='p3', password='password123'),
    User.objects.create_user(username='p4', password='password123'),
    User.objects.create_user(username='p5', password='password123'),
    User.objects.create_user(username='p6', password='password123'),
    User.objects.create_user(username='p7', password='password123'),
]

# CONTACT PERSON
cp1 = Contact_Person.objects.create(contact_person_id=10000, first_name='Josh', middle_name='Yu', last_name='Lewis', contact_email='test@gmail.com', contact_number='091-715-914')
cp2 = Contact_Person.objects.create(contact_person_id=10001, first_name='Maria', middle_name='Reyes', last_name='Lopez', contact_email='test@gmail.com', contact_number='091-715-914')
cp3 = Contact_Person.objects.create(contact_person_id=10002, first_name='Jose', middle_name='Garcia', last_name='Tan', contact_email='test@gmail.com', contact_number='091-715-914')
cp4 = Contact_Person.objects.create(contact_person_id=10003, first_name='Ana', middle_name='Cruz', last_name='Santos', contact_email='test@gmail.com', contact_number='091-715-914')
cp5 = Contact_Person.objects.create(contact_person_id=10004, first_name='Luis', middle_name='Martinez', last_name='De la Vega', contact_email='test@gmail.com', contact_number='091-715-914')
cp6 = Contact_Person.objects.create(contact_person_id=10005, first_name='Andrea', middle_name='Villanueva', last_name='Lim', contact_email='test@gmail.com', contact_number='091-715-914')
cp7 = Contact_Person.objects.create(contact_person_id=10006, first_name='Carlos', middle_name='Neri', last_name='Chua', contact_email='test@gmail.com', contact_number='091-715-914')

# ORGANIZERS 
org1 = Organizer.objects.create(user=users[0], organizer_id=10000, name='Computer Society of the Ateneo', organizer_type='INTERNAL', contact_person=cp1, street='Katipunan Avenue', barangay='Loyola Heights', city='Quezon City', region='Metro Manila')
org2 = Organizer.objects.create(user=users[1], organizer_id=10001, name='Ateneo Mathematics Society', organizer_type='INTERNAL', contact_person=cp2, street='Katipunan Avenue', barangay='Loyola Heights', city='Quezon City', region='Metro Manila')
org3 = Organizer.objects.create(user=users[2], organizer_id=10002, name='UPTC Market', organizer_type='EXTERNAL', contact_person=cp3, street='Katipunan Avenue', barangay='Loyola Heights', city='Quezon City', region='Metro Manila')
org4 = Organizer.objects.create(user=users[3], organizer_id=10003, name='The Tech Bros', organizer_type='EXTERNAL', contact_person=cp4, street='Street 4', barangay='Brgy 4', city='QC', region='NCR')
org5 = Organizer.objects.create(user=users[4], organizer_id=10004, name='Collegiate Society of Advertising', organizer_type='INTERNAL', contact_person=cp5, street='Katipunan Avenue', barangay='Loyola Heights', city='Quezon City', region='Metro Manila')
org6 = Organizer.objects.create(user=users[5], organizer_id=10005, name='Health Science Society', organizer_type='INTERNAL', contact_person=cp6, street='Katipunan Avenue', barangay='Loyola Heights', city='Quezon City', region='Metro Manila')
org7 = Organizer.objects.create(user=users[6], organizer_id=10006, name='Council of Organizations of the Ateneo', organizer_type='EXTERNAL', contact_person=cp7, street='Katipunan Avenue', barangay='Loyola Heights', city='Quezon City', region='Metro Manila')

# BUILDINGS
b1 = Building.objects.create(building_id=10000, building_name='Berchman Hall')
b2 = Building.objects.create(building_id=10001, building_name='Faura Hall')
b3 = Building.objects.create(building_id=10002, building_name='SEC-A')
b4 = Building.objects.create(building_id=10003, building_name='SEC-B')
b5 = Building.objects.create(building_id=10004, building_name='The Loft, Arete')
b6 = Building.objects.create(building_id=10005, building_name='Bellarmine Hall')
b7 = Building.objects.create(building_id=10006, building_name='Leong Hall Auditorium')

# LOCATIONS
loc1 = Location.objects.create(location_id=10000, building=b1, room_name='Room 101', max_capacity=30)
loc2 = Location.objects.create(location_id=10001, building=b2, room_name='Room 102', max_capacity=30)
loc3 = Location.objects.create(location_id=10002, building=b3, room_name='Room 103', max_capacity=30)
loc4 = Location.objects.create(location_id=10003, building=b4, room_name='Room 104', max_capacity=30)
loc5 = Location.objects.create(location_id=10004, building=b5, room_name=None, max_capacity=100)
loc6 = Location.objects.create(location_id=10005, building=b6, room_name='Room 105', max_capacity=30)
loc7 = Location.objects.create(location_id=10006, building=b7, room_name=None, max_capacity=100)

# ACTIVITIES
act1 = Activity.objects.create(activity_id=10000, activity_name='Dev Workshops', organizer=org1)
act2 = Activity.objects.create(activity_id=10001, activity_name='LaTeX Seminar', organizer=org2)
act3 = Activity.objects.create(activity_id=10002, activity_name='Jolly Market', organizer=org3)
act4 = Activity.objects.create(activity_id=10003, activity_name='Arete Art Walk', organizer=org5)
act5 = Activity.objects.create(activity_id=10004, activity_name='Calculus for Beginners', organizer=org2)
act6 = Activity.objects.create(activity_id=10005, activity_name='Love Yourself Campaign', organizer=org6)
act7 = Activity.objects.create(activity_id=10006, activity_name='Christmas Fundraiser', organizer=org7)

# ------------------
# SCHEDULES (7)
# ------------------
sched1 = Activity_Schedule.objects.create(schedule_ID=10000, date='2025-10-07', start_time='17:00', end_time='18:30', expected_participants=0, location=loc1, activity=act1)
sched2 = Activity_Schedule.objects.create(schedule_ID=10001, date='2025-10-17', start_time='17:00', end_time='20:00', expected_participants=0, location=loc2, activity=act2)
sched3 = Activity_Schedule.objects.create(schedule_ID=10002, date='2025-11-15', start_time='08:00', end_time='22:00', expected_participants=0, location=loc3, activity=act3)
sched4 = Activity_Schedule.objects.create(schedule_ID=10003, date='2025-11-08', start_time='08:00', end_time='10:00', expected_participants=0, location=loc4, activity=act4)
sched5 = Activity_Schedule.objects.create(schedule_ID=10004, date='2025-11-25', start_time='15:00', end_time='17:00', expected_participants=0, location=loc4, activity=act5)
sched6 = Activity_Schedule.objects.create(schedule_ID=10005, date='2025-12-06', start_time='11:00', end_time='17:00', expected_participants=0, location=loc6, activity=act6)
sched7 = Activity_Schedule.objects.create(schedule_ID=10006, date='2025-12-06', start_time='11:00', end_time='17:00', expected_participants=0, location=loc7, activity=act7)

# DEPARTMENTS
dep1 = Department.objects.create(department_ID=10000, department_name='Computer Science and Information Systems')
dep2 = Department.objects.create(department_ID=10001, department_name='Mathematics')
dep3 = Department.objects.create(department_ID=10002, department_name='Biology')
dep4 = Department.objects.create(department_ID=10003, department_name='Physics')
dep5 = Department.objects.create(department_ID=10004, department_name='Philosophy')
dep6 = Department.objects.create(department_ID=10005, department_name='Theology')
dep7 = Department.objects.create(department_ID=10006, department_name='Chemistry')

# PARTICIPANT
p1 = Participant.objects.create(participant_ID=10000, user=users[7], first_name='Madeline', middle_name='Hollow', last_name='Yao', birth_date='2002-05-12', participant_type='ST', department=dep1)
p2 = Participant.objects.create(participant_ID=10001, user=users[8], first_name='Chris', middle_name='Tan', last_name='Ario', birth_date='1998-11-03', participant_type='FM', department=dep2)
p3 = Participant.objects.create(participant_ID=10002, user=users[9], first_name='Torry', middle_name='Davis', last_name='Santos', birth_date='2001-07-22', participant_type='ST', department=dep3)
p4 = Participant.objects.create(participant_ID=10003, user=users[10], first_name='Gab', middle_name='Syd', last_name='Yap', birth_date='1999-03-09', participant_type='SM', department=dep4)
p5 = Participant.objects.create(participant_ID=10004, user=users[11], first_name='Luke', middle_name='Mendoza', last_name='Lim', birth_date='2000-12-12', participant_type='FM', department=dep5)
p6 = Participant.objects.create(participant_ID=10005, user=users[12], first_name='Frank', middle_name='la', last_name='Torres', birth_date='1997-08-21', participant_type='ST', department=dep6)
p7 = Participant.objects.create(participant_ID=10006, user=users[13], first_name='Megan', middle_name='Lee', last_name='Choi', birth_date='2002-10-10', participant_type='ST', department=dep7)

# ACTIVITY BOOKINGS 
Activity_Booking.objects.create(booking_ID=10000, schedule=sched1, participant=p1, has_attended=True)
Activity_Booking.objects.create(booking_ID=10001, schedule=sched1, participant=p2, has_attended=False)
Activity_Booking.objects.create(booking_ID=10002, schedule=sched2, participant=p3, has_attended=True)
Activity_Booking.objects.create(booking_ID=10003, schedule=sched3, participant=p4, has_attended=True)
Activity_Booking.objects.create(booking_ID=10004, schedule=sched4, participant=p5, has_attended=False)
Activity_Booking.objects.create(booking_ID=10005, schedule=sched5, participant=p6, has_attended=True)
Activity_Booking.objects.create(booking_ID=10006, schedule=sched6, participant=p7, has_attended=False)

for schedule in Activity_Schedule.objects.all():
    schedule.expected_participants = schedule.activity_booking_set.count()
    schedule.save()

print("updated expected participants")
print("DATABASE POPULATED SUCCESSFULLY!")
