from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator


ORGANIZER_TYPE = ( 
    ('INTERNAL', 'Internal'),
    ('EXTERNAL', 'External')
)

PARTICIPANT_TYPE = (
    ('ST', 'Student'),
    ('FM', 'Faculty'),
    ('SM', 'Staff Member')
)

class Contact_Person(models.Model):
    contact_person_id = models.AutoField(primary_key=True, validators=[MinValueValidator(10000), MaxValueValidator(99999)])
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    contact_email = models.EmailField(max_length=255)
    contact_number = models.CharField(max_length=11,  
                                        validators=[
                                            RegexValidator(
                                                regex=r'^\d{3}-\d{3}-\d{3}$',
                                                message='Contact number must be in XXX-XXX-XXX format'
                                            )]
                                        )   
    def __str__(self):      
        return f"{self.first_name} {self.middle_name} {self.last_name}"


class Organizer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organizer_id = models.AutoField(primary_key=True, validators=[MinValueValidator(10000), MaxValueValidator(99999)])
    name = models.CharField(max_length=255)
    organizer_type = models.CharField(max_length=8, choices=ORGANIZER_TYPE, default="EXTERNAL")
    contact_person = models.ForeignKey(Contact_Person, on_delete=models.SET_NULL, null=True)
    street = models.CharField(max_length=255)
    barangay = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Building(models.Model):
    building_id = models.AutoField(primary_key=True, validators=[MinValueValidator(10000), MaxValueValidator(99999)])
    building_name = models.CharField(max_length=255)
    def __str__(self):      
        return self.building_name

class Location(models.Model):
    location_id = models.AutoField(primary_key=True, validators=[MinValueValidator(10000), MaxValueValidator(99999)])
    building = models.ForeignKey(Building, on_delete=models.SET_NULL, null=True)
    room_name = models.CharField(max_length=255, blank=True, null=True)
    max_capacity = models.IntegerField()
    def __str__(self):
        return f"{self.building}: {self.room_name}"

class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    activity_name = models.CharField(max_length=255)
    def __str__(self):
        return self.activity_name
    
class Activity_Schedule(models.Model):
    schedule_ID = models.AutoField(primary_key=True, validators=[MinValueValidator(10000), MaxValueValidator(99999)])
    date = models.DateField()    
    start_time = models.TimeField()
    end_time = models.TimeField()
    expected_participants = models.IntegerField(default=0)
    organizer = models.ForeignKey(Organizer,  on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Location,  on_delete=models.SET_NULL, null=True)
    activity = models.ForeignKey(Activity,  on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.activity} on {self.date} at {self.start_time}"

class Department(models.Model):
    department_ID = models.AutoField(primary_key=True, validators=[MinValueValidator(10000), MaxValueValidator(99999)])
    department_name = models.CharField(max_length=255)
    def __str__(self):
        return self.department_name

class Participant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    participant_ID=models.AutoField(primary_key=True, validators=[MinValueValidator(10000), MaxValueValidator(99999)])
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    participant_type = models.CharField(max_length=12, choices=PARTICIPANT_TYPE)                   #PLACEHOLDER: IDK HOW TO implement the subtype supertype thing
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"
        
class Activity_Booking(models.Model):
    booking_ID = models.AutoField(primary_key=True, validators=[MinValueValidator(10000), MaxValueValidator(99999)])
    has_attended = models.BooleanField()
    booking_date = models.DateField(auto_now_add=True)
    schedule = models.ForeignKey(Activity_Schedule, on_delete=models.SET_NULL, null=True)
    participant = models.ForeignKey(Participant, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.participant} booking for {self.schedule}"


