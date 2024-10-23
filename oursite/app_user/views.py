from django.shortcuts import render
from django.http import HttpResponse
from app_user.models import user,faculty
from app_admin.models import admin_acc

# Create your views here.
def index(request) :
    all_user = user.objects.all()
    return render(request,"index.html",{"all_user":all_user})

def profile(request) :
    return render(request,"profile.html")

def booking(request) :
    return render(request,"booking.html")

def contact(request) :
    admins = admin_acc.objects.all()
    return render(request,"contact.html",{"admins":admins})

def report(request) :
    return render(request,"report.html")

def register(request) :
    all_faculty = faculty.objects.all()
    return render(request,"forms/register.html",{"all_faculty":all_faculty})

def calendar(request) :
    return render(request,"forms/calendar.html")