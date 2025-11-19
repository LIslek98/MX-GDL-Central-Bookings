"""Create models Organizer & Activity with appropriate fields."""
from django.db import models
class Contact_Person(models.Model):
    contact_person_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=255)
    contact_email = models.EmailField(max_length=255)
    contact_number = models.IntegerField()          #this is so ugly ngl
    def __str__(self):
        """Return the name of the Contact Person."""
        return self.contact_name


class Organizer(models.Model):
    """Create ArticleCategory with appropriate field, sorted alphabetically."""
    organizer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    organizer_type = models.CharField(max_length=255)
    contact_person = models.ForeignKey(Contact_Person, on_delete=models.SET_NULL, null=True)#idk how to connect foreign key to primary key, I think with django you just connect foreign key to entity? This is originally contact_person_id
    address = models.CharField(max_length=255)
    def __str__(self):
        """Return the name of the Article Category."""
        return self.name
    class Meta:
        """Order the article categorys alphabetically."""
        ordering = ["name"]

class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=255)
    max_capacity = models.IntegerField()
    def __str__(self):
        return self.room_name

class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    building = models.CharField(max_length=255) #building_name
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.building

class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    activity_name = models.CharField(max_length=255)
    def __str__(self):
        return self.activity_name
    
class Activity_Schedule(models.Model):
    schedule_ID = models.AutoField(primary_key=True)
    date = models.DateField()       #IDK IF THIS WORKS AS A COMPOSITE
    start_time = models.TimeField()
    end_time = models.TimeField()
    expected_participants = models.IntegerField(default=0)
    organizer = models.ForeignKey(Organizer,  on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Location,  on_delete=models.SET_NULL, null=True)
    activity = models.ForeignKey(Activity,  on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.activity} on {self.date} at {self.start_time}"

class Department(models.Model):
    department_ID = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=255)
    def __str__(self):
        return self.department_name

class Participant(models.Model):
    participant_ID=models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    participant_type = models.CharField()                   #PLACEHOLDER: IDK HOW TO implement the subtype supertype thing
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name

class Activity_Booking(models.Model):
    booking_ID = models.AutoField(primary_key=True)
    has_attended = models.BooleanField()
    booking_date = models.DateField()
    schedule = models.ForeignKey(Activity_Schedule, on_delete=models.SET_NULL, null=True)
    participant = models.ForeignKey(Participant, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.participant} booking for {self.schedule}"
