from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse

returning_choices =(
(0, ''),
(1, 'Yes'),
(2, 'No'),
)

# Create your models here.
class Player(models.Model):
    GuardianFirstName = models.CharField('Guardian First Name', max_length=300)
    GuardianLastName = models.CharField('Guardian Last Name', max_length=300)
    PlayerFirstName = models.CharField('Player First Name', max_length=300)
    PlayerLastName = models.CharField('Player Last Name', max_length=300)
    DateOfBirth = models.DateField('Date of Birth')
    Street = models.CharField(max_length=300)
    City = models.CharField(max_length=300)
    State = models.CharField(max_length=300)
    Zipcode = models.IntegerField()
    PhoneNumber = models.IntegerField('Phone Number')
    Level = models.CharField(max_length=300)

    def __unicode__(self):
        return self.GuardianLastName

class Volunteer(models.Model):
    FirstName = models.CharField('First Name', max_length=300)
    LastName = models.CharField('Last Name', max_length=300)
    DateOfBirth = models.DateField('Date of Birth')
    Street = models.CharField(max_length=300)
    City = models.CharField(max_length=300)
    State = models.CharField(max_length=300)
    Zipcode = models.IntegerField()
    PhoneNumber = models.IntegerField('Phone Number')
    Email = models.EmailField(max_length=300)
    Returning = models.IntegerField(choices=returning_choices, default=0)
    Children = models.IntegerField(null=True)

    def __unicode__(self):
        return self.LastName

class Field(models.Model):
    FieldName = models.CharField(max_length=100)
    Street = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.FieldName
        
    def get_absolute_url(self):
        return reverse('field_detail', args=[self.id])

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
    FieldID = models.ForeignKey(Field)
    VolunteerID = models.ForeignKey(Volunteer)
    
class Update(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.title