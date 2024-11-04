from django.shortcuts import render, redirect
from app_user.models import faculty
from app_admin.models import room, admin_acc, category
# Create your views here.
def index(request) :
    return render(request,"adminpage.html")
def form_cat(request) :
    facultys = faculty.objects.all()
    return render(request,"forms/category.html",{"facultys":facultys})
def form_room(request) :
    if request.method == "POST" :
        roomname = request.POST["roomname"]
        approved = request.POST["approved"]
        unapproved = request.POST["unapproved"]
        address = request.POST["address"]
        # start_hour = request.POST["start_hour"]
        # start_minute = request.POST["start_minute"]
        # emd_hour = request.POST["end_hpur"]
        # end_minute = request.POST["end_minute"]
        img = request.FILES["img"]
        note = request.POST["note"]
        time = request.POST["timelength"]
        categorys = request.POST["category"]
        rooms = room.objects.create(
            roomname = roomname, 
            timelength = time,
            approval = approved,
            description =note,
            address = address,
            img = img,
            admin = admin_acc.objects.get(adminid = 1),
            category = category.object.get(id = categorys)
        )
        rooms.save()
        return redirect("/admin")
    else :
        return render(request,"forms/rooms.html")
    
