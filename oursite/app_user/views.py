from django.shortcuts import render, redirect
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
    if request.method == "POST":
        username = request.POST["username"]
        studentid = request.POST["code"]
        name = request.POST["name"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        facultys = request.POST["faculty"]
        img = request.FILES["img"]
        major = request.POST["major"]
        User = user.objects.create(
            code = studentid,
            username = username,
            name = name,
            lastname = lastname,
            password = password,
            faculty = facultys,
            img = img,
            major = major
        )
        User.save()
        return redirect('')
    return render(request,"forms/register.html",{"all_faculty":all_faculty})

def calendar(request) :
    return render(request,"forms/calendar.html")