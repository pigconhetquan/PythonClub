from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    meetinglocation=models.CharField(max_length=255)
    agenda=models.TextField()

    def __str__(self):
        return self.meetingtitle

    class Meta:
        db_table='meeting'

class MeetingMinutes(models.Model):
    meetingid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User)
    minutestext=models.TextField()

    def __str__(self):
        return self.minutestext

    class Meta:
        db_table='meetingminutes'

class Resources(models.Model):
    resourcename=models.CharField(max_length=300)
    resourcetype=models.CharField(max_length=300)
    url=models.URLField(null=True, blank=True)
    dateentered=models.DateField()
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description=models.TextField()

    def __str__(self):
        return self.resourcename
    
    class Meta:
        db_table='resources'

class Event(models.Model):
    eventtitle=models.CharField(max_length=300)
    eventlocation=models.CharField(max_length=300)
    eventdate=models.DateField()
    eventtime=models.TimeField()
    eventdescription=models.TextField()
    eventuserid=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.eventtitle
    
    class Meta:
        db_table='event'