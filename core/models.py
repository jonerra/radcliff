from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

FIELDS = (
(0, ''),
(1, 'Field 1'),
(2, 'Field 2'),
(3, 'Field 3'),
(4, 'Field 4'),
)

DATES = (
(0, ''),
(1, '8:00AM - 10:00AM'),
(2, '10:00AM - 12:00PM'),
(3, '12:00PM - 2:00PM'),
(4, '2:00PM - 4:00PM'),
(5, '4:00PM - 6:00PM'),
(6, '6:00PM - 8:00PM'),
)

# Create your models here.
class Player(models.Model):
    GuardianFirstName = models.CharField(max_length=300)
    GuardianLastName = models.CharField(max_length=300)
    PlayerFirstName = models.CharField(max_length=300)
    PlayerLastName = models.CharField(max_length=300)
    DateOfBirth = models.DateField()
    Street = models.CharField(max_length=300)
    City = models.CharField(max_length=300)
    State = models.CharField(max_length=300)
    Zipcode = models.IntegerField()
    PhoneNumber = models.IntegerField()
    Level = models.CharField(max_length=300)

    def __unicode__(self):
        return self.GuardianLastName

class Volunteer(models.Model):
    FirstName = models.CharField(max_length=300)
    LastName = models.CharField(max_length=300)
    DateOfBirth = models.DateField()
    Street = models.CharField(max_length=300)
    City = models.CharField(max_length=300)
    State = models.CharField(max_length=300)
    Zipcode = models.IntegerField()
    PhoneNumber = models.IntegerField()
    Email = models.EmailField(max_length=300)
    Returning = models.CharField(max_length=300)
    Children = models.CharField(max_length=300)

    def __unicode__(self):
        return self.LastName

class Field(models.Model):
    Location = models.CharField(max_length=100)
    Fieldsize = models.CharField(max_length=300)

class Position(models.Model):
    PositionDescrip = models.CharField(max_length=300)

class VolunteerAssignment(models.Model):
    VolunteerID = models.ForeignKey(Volunteer)
    PositionID = models.ForeignKey(Position)
    Year = models.IntegerField()

class Division(models.Model):
    Level = models.CharField(max_length=300)

class Team(models.Model):
    TeamName = models.CharField(max_length=50)
    VolunteerID = models.ForeignKey(Volunteer)
    DivisionID = models.ForeignKey(Division)
    Year = models.IntegerField()

class Roster(models.Model):
    TeamID = models.ForeignKey(Team)
    PlayerID = models.ForeignKey(Player)

class Reservation(models.Model):
    FieldName = models.IntegerField(choices=FIELDS, default=0)
    Date = models.IntegerField(choices=DATES, default=0, unique=True)
    # FieldID = models.ForeignKey(Field)
    # VolunteerID = models.ForeignKey(Volunteer)
    
class Update(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.title