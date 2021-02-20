from django import forms
from .models import Meeting, MeetingMinutes, Resources, Event

class MeetingForm(forms.ModelForm):
    class Meta:
        model=Meeting
        fields='__all__'

class ResourcesForm(forms.ModelForm):
    class Meta:
        model=Resources
        fields='__all__'