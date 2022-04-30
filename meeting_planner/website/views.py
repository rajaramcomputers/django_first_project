from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from meetings.models import Meeting, Room
from staffleave.models import leaveapplied
from staffleave.models import staffdetails
# Create your views here.
# def welcome(request):
#     return render(request,'website/welcome.html',
#                   {"message": "Total Number of Meeting Registered",
#                   "x":42, "num_of_meetings":Meeting.objects.count()})
def welcome(request):
    return render(request,"website/welcome.html",
                  {"meetings": Meeting.objects.all()})


def staffleave(request):
    return render(request, "website/staffleave.html",
                  {"staffleave": leaveapplied.objects.all().prefetch_related('staffid')
})
def date(request):
    return HttpResponse("This page was server at" + str(datetime.now()))

def about(request):
    return render(request,'website/about.html',
    {"name":"Dr Ramkumar"})

def contactus(request):
    return HttpResponse('<h2>Visit University of Technology and Applied Sciences')

def product(request):
    return HttpResponse('<h2>This is a product page </h2>')
