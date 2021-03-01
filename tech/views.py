from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resources, Event
from django.urls import reverse_lazy
from .forms import MeetingForm, ResourcesForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'tech/index.html')

def resources(request):
    resource_list=Resources.objects.all()
    return render(request, 'tech/resources.html', {'resource_list': resource_list})

def meeting(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'tech/meeting.html', {'meeting_list': meeting_list})

def meetingDetail(request, id):
    meeting=get_object_or_404(Meeting, pk=id)
    return render(request, 'tech/meetingdetail.html', {'meeting' : meeting})

def resourcesDetail(request, id):
    resources=get_object_or_404(Resources, pk=id)
    return render(request, 'tech/resourcesdetail.html', {'resources':resources})

@login_required
def newMeeting(request):
    form=MeetingForm

    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'tech/newmeeting.html', {'form': form})

def newResources(request):
    form=ResourcesForm
    if request.method=='POST':
        form=ResourcesForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourcesForm()
    else:
        form=ResourcesForm()
    return render(request, 'tech/newresources.html', {'form': form})

def loginmessage(request):
    return render(request, 'tech/loginmessage.html')

def logoutmessage(request):
    return render(request, 'tech/logoutmessage.html')