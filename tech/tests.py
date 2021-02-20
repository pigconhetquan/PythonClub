from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resources, Event
import datetime
from .forms import MeetingForm
# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.type=Meeting(meetingtitle='Game Day')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Game Day')
    
    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinutesTest(TestCase):
    def setUp(self):
        self.type = Meeting(meetingtitle='Game Day')
        self.minutestext= MeetingMinutes(minutestext= '2 hours', meetingid =self.type)
        
    def test_typestring(self):
        self.assertEqual(str(self.minutestext), '2 hours')

    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

class ResourcesTest(TestCase):
    def setUp(self):
        self.name = Resources(resourcename = 'Keyboard')
        self.user = User(username= 'ironman')
        self.resource = Resources(resourcename= self.name, resourcetype='Corsair', url='https://www.corsair.com/us/en/', dateentered='2021-02-04', userid=self.user, description='good keyboard')

    def test_typestring(self):
        self.assertEqual(str(self.name), 'Keyboard')

    def test_tablename(self):
        self.assertEqual(str(Resources._meta.db_table), 'resources')

class EventTest(TestCase):
    def setUp(self):
        self.title = Event(eventtitle='Game Day')
        self.user = User(username='batman')
        self.event = Event(eventtitle=self.title, eventlocation='Room 1110', eventdate='2021-01-04', eventtime='18:00', eventdescription='Playing game', eventuserid=self.user)

    def test_typestring(self):
        self.assertEqual(str(self.title),'Game Day')

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

class NewMeetingForm(TestCase):
    def test_meetingform(self):
        data={
            'meetingtitle':'party', 
            'meetingdate':'2021-06-06', 
            'meetingtime':'20:00:00', 
            'meetinglocation':'Room 1110', 
            'agenda':'Mid Year Party'
        }
        form=MeetingForm(data)
        self.assertTrue(form.is_valid)

    def test_meetingform_Invalid(self):
        data={
            'meetingtitle':'', 
            'meetingdate':'',
            'meetingtime':'',
            'meetinglocation':'',
            'agenda':'' 
        }
        form=MeetingForm(data)
        self.assertFalse(form.is_valid())