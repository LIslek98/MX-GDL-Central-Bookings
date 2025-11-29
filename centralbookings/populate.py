import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'centralbookings.settings')
django.setup()

from django.contrib.auth.models import User
from UserManagement.models import (
    Contact_Person, Organizer, Building, Location, Activity,
    Activity_Schedule, Department, Participant, Activity_Booking
)

# ------------------
# CLEAR OLD DATA
# ------------------
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

# ------------------
# USERS (14: 7 organizers + 7 participants)
# ------------------
users = [
    # Organizers
    User.objects.create_user(username='org1', password='password123'),
    User.objects.create_user(username='org2', password='password123'),
    User.objects.create_user(username='org3', password='password123'),
    User.objects.create_user(username='org4', password='password123'),
    User.objects.create_user(username='org5', password='password123'),
    User.objects.create_user(username='org6', password='password123'),
    User.objects.create_user(username='org7', password='password123'),

    # Participants
    User.objects.create_user(username='p1', password='password123'),
    User.objects.create_user(username='p2', password='password123'),
    User.objects.create_user(username='p3', password='password123'),
    User.objects.create_user(username='p4', password='password123'),
    User.objects.create_user(username='p5', password='password123'),
    User.objects.create_user(username='p6', password='password123'),
    User.objects.create_user(username='p7', password='password123'),
]

# ------------------
# CONTACT PERSONS (7)
# ------------------
cp1 = Contact_Person.objects.create(contact_person_id=10001, first_name='Juan', middle_name='Santos', last_name='Dela Cruz', contact_email='juan@example.com', contact_number='091-712-345')
cp2 = Contact_Person.objects.create(contact_person_id=10002, first_name='Maria', middle_name='Reyes', last_name='Lopez', contact_email='maria@example.com', contact_number='091-812-345')
cp3 = Contact_Person.objects.create(contact_person_id=10003, first_name='Jose', middle_name='Garcia', last_name='Tan', contact_email='jose@example.com', contact_number='091-912-345')
cp4 = Contact_Person.objects.create(contact_person_id=10004, first_name='Ana', middle_name='Cruz', last_name='Santos', contact_email='ana@example.com', contact_number='092-012-345')
cp5 = Contact_Person.objects.create(contact_person_id=10005, first_name='Luis', middle_name='Martinez', last_name='De la Vega', contact_email='luis@example.com', contact_number='092-112-345')
cp6 = Contact_Person.objects.create(contact_person_id=10006, first_name='Andrea', middle_name='Villanueva', last_name='Lim', contact_email='andrea@example.com', contact_number='092-212-345')
cp7 = Contact_Person.objects.create(contact_person_id=10007, first_name='Carlos', middle_name='Neri', last_name='Chua', contact_email='carlos@example.com', contact_number='092-312-345')

# ------------------
# ORGANIZERS (7)
# ------------------
org1 = Organizer.objects.create(user=users[0], organizer_id=20001, name='Computer Society', organizer_type='INTERNAL', contact_person=cp1, street='Street 1', barangay='Brgy 1', city='QC', region='NCR')
org2 = Organizer.objects.create(user=users[1], organizer_id=20002, name='Ateneo Athletics', organizer_type='INTERNAL', contact_person=cp2, street='Street 2', barangay='Brgy 2', city='QC', region='NCR')
org3 = Organizer.objects.create(user=users[2], organizer_id=20003, name='Blue Market', organizer_type='EXTERNAL', contact_person=cp3, street='Street 3', barangay='Brgy 3', city='QC', region='NCR')
org4 = Organizer.objects.create(user=users[3], organizer_id=20004, name='Tech Innovators', organizer_type='EXTERNAL', contact_person=cp4, street='Street 4', barangay='Brgy 4', city='QC', region='NCR')
org5 = Organizer.objects.create(user=users[4], organizer_id=20005, name='Art Club', organizer_type='INTERNAL', contact_person=cp5, street='Street 5', barangay='Brgy 5', city='QC', region='NCR')
org6 = Organizer.objects.create(user=users[5], organizer_id=20006, name='Science Guild', organizer_type='INTERNAL', contact_person=cp6, street='Street 6', barangay='Brgy 6', city='QC', region='NCR')
org7 = Organizer.objects.create(user=users[6], organizer_id=20007, name='Community Org', organizer_type='EXTERNAL', contact_person=cp7, street='Street 7', barangay='Brgy 7', city='QC', region='NCR')

# ------------------
# BUILDINGS (7)
# ------------------
b1 = Building.objects.create(building_id=30001, building_name='Faber Hall')
b2 = Building.objects.create(building_id=30002, building_name='Gonzaga Hall')
b3 = Building.objects.create(building_id=30003, building_name='SEC A')
b4 = Building.objects.create(building_id=30004, building_name='SEC B')
b5 = Building.objects.create(building_id=30005, building_name='Ricardo Hall')
b6 = Building.objects.create(building_id=30006, building_name='Bellarmine Hall')
b7 = Building.objects.create(building_id=30007, building_name='Leong Hall')

# ------------------
# LOCATIONS (7)
# ------------------
loc1 = Location.objects.create(location_id=40001, building=b1, room_name='Room 101', max_capacity=30)
loc2 = Location.objects.create(location_id=40002, building=b2, room_name='Room 202', max_capacity=50)
loc3 = Location.objects.create(location_id=40003, building=b3, room_name=None, max_capacity=200)
loc4 = Location.objects.create(location_id=40004, building=b4, room_name='Lab 1', max_capacity=25)
loc5 = Location.objects.create(location_id=40005, building=b5, room_name='Studio 5', max_capacity=40)
loc6 = Location.objects.create(location_id=40006, building=b6, room_name='Room 301', max_capacity=35)
loc7 = Location.objects.create(location_id=40007, building=b7, room_name=None, max_capacity=300)

# ------------------
# ACTIVITIES (7)
# ------------------
act1 = Activity.objects.create(activity_id=50001, activity_name='Coding Workshop', organizer=org1)
act2 = Activity.objects.create(activity_id=50002, activity_name='Math Lecture', organizer=org2)
act3 = Activity.objects.create(activity_id=50003, activity_name='Robotics Expo', organizer=org3)
act4 = Activity.objects.create(activity_id=50004, activity_name='Art Exhibit', organizer=org5)
act5 = Activity.objects.create(activity_id=50005, activity_name='Football Training', organizer=org2)
act6 = Activity.objects.create(activity_id=50006, activity_name='Science Talk', organizer=org6)
act7 = Activity.objects.create(activity_id=50007, activity_name='Community Meetup', organizer=org7)

# ------------------
# SCHEDULES (7)
# ------------------
sched1 = Activity_Schedule.objects.create(schedule_ID=60001, date='2025-12-01', start_time='09:00', end_time='11:00', expected_participants=0, location=loc1, activity=act1)
sched2 = Activity_Schedule.objects.create(schedule_ID=60002, date='2025-12-02', start_time='10:00', end_time='12:00', expected_participants=0, location=loc2, activity=act2)
sched3 = Activity_Schedule.objects.create(schedule_ID=60003, date='2025-12-03', start_time='14:00', end_time='17:00', expected_participants=0, location=loc3, activity=act3)
sched4 = Activity_Schedule.objects.create(schedule_ID=60004, date='2025-12-04', start_time='08:00', end_time='10:00', expected_participants=0, location=loc5, activity=act4)
sched5 = Activity_Schedule.objects.create(schedule_ID=60005, date='2025-12-05', start_time='15:00', end_time='17:00', expected_participants=0, location=loc7, activity=act5)
sched6 = Activity_Schedule.objects.create(schedule_ID=60006, date='2025-12-06', start_time='11:00', end_time='13:00', expected_participants=0, location=loc4, activity=act6)
sched7 = Activity_Schedule.objects.create(schedule_ID=60007, date='2025-12-07', start_time='13:00', end_time='16:00', expected_participants=0, location=loc7, activity=act7)

# ------------------
# DEPARTMENTS (7)
# ------------------
dep1 = Department.objects.create(department_ID=70001, department_name='Computer Science')
dep2 = Department.objects.create(department_ID=70002, department_name='Mathematics')
dep3 = Department.objects.create(department_ID=70003, department_name='Biology')
dep4 = Department.objects.create(department_ID=70004, department_name='Physics')
dep5 = Department.objects.create(department_ID=70005, department_name='Economics')
dep6 = Department.objects.create(department_ID=70006, department_name='Fine Arts')
dep7 = Department.objects.create(department_ID=70007, department_name='Chemistry')

# ------------------
# PARTICIPANTS (7)
# ------------------
p1 = Participant.objects.create(participant_ID=80001, user=users[7], first_name='Alice', middle_name='May', last_name='Reyes', birth_date='2002-05-12', participant_type='ST', department=dep1)
p2 = Participant.objects.create(participant_ID=80002, user=users[8], first_name='Bob', middle_name='Lao', last_name='Tan', birth_date='1998-11-03', participant_type='FM', department=dep2)
p3 = Participant.objects.create(participant_ID=80003, user=users[9], first_name='Charlie', middle_name='Pascual', last_name='Santos', birth_date='2001-07-22', participant_type='ST', department=dep3)
p4 = Participant.objects.create(participant_ID=80004, user=users[10], first_name='David', middle_name='Ramos', last_name='Yap', birth_date='1999-03-09', participant_type='SM', department=dep4)
p5 = Participant.objects.create(participant_ID=80005, user=users[11], first_name='Ella', middle_name='Mendoza', last_name='Lim', birth_date='2000-12-12', participant_type='FM', department=dep5)
p6 = Participant.objects.create(participant_ID=80006, user=users[12], first_name='Frank', middle_name='Cruz', last_name='Torres', birth_date='1997-08-21', participant_type='ST', department=dep6)
p7 = Participant.objects.create(participant_ID=80007, user=users[13], first_name='Grace', middle_name='Lee', last_name='Choi', birth_date='2002-10-10', participant_type='ST', department=dep7)

# ------------------
# BOOKINGS (7)
# ------------------
Activity_Booking.objects.create(booking_ID=90001, schedule=sched1, participant=p1, has_attended=True)
Activity_Booking.objects.create(booking_ID=90002, schedule=sched1, participant=p3, has_attended=False)
Activity_Booking.objects.create(booking_ID=90003, schedule=sched2, participant=p2, has_attended=True)
Activity_Booking.objects.create(booking_ID=90004, schedule=sched3, participant=p4, has_attended=True)
Activity_Booking.objects.create(booking_ID=90005, schedule=sched4, participant=p5, has_attended=False)
Activity_Booking.objects.create(booking_ID=90006, schedule=sched5, participant=p6, has_attended=True)
Activity_Booking.objects.create(booking_ID=90007, schedule=sched6, participant=p7, has_attended=False)

for schedule in Activity_Schedule.objects.all():
    schedule.expected_participants = schedule.activity_booking_set.count()
    schedule.save()

print("updated expected participants")
print("DATABASE POPULATED SUCCESSFULLY!")
