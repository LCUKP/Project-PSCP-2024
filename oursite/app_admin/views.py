from django.shortcuts import render,redirect
from app_user.models import faculty
from app_admin.models import room, admin_acc, category
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def index(request) :
    return render(request,"adminpage.html")
def admin_manage(request) :
    return render(request,"admin_manager.html")
def history(request) :
    return render(request,"booking_history.html")
def form_cat(request) :
    if request.method == "POST" :
        catname = request.POST["catname"]
        address = request.POST["address"]
        fac = request.POST["fac"]
        businesshoursin = request.POST["businesshoursin"]
        businesshoursout = request.POST["businesshoursout"]
        time = f"{businesshoursin}-{businesshoursout}"
        img = request.FILES["img"]
        note = request.POST["note"]
        cat = category.objects.create(
            catname = catname,
            permission = fac,
            img = img,
            admin = admin_acc.objects.get(adminid = 1),
            address = address,
            time = time,
            note = note,
        )
        cat.save()
        return redirect("/admin/")
    else :
        facultys = faculty.objects.all()
        return render(request,"forms/category.html",{"facultys":facultys})
def form_room(request) :
    if request.method == "POST" :
        roomname = request.POST["roomname"]
        approved = request.POST["approved"] == "true"
        address = request.POST["address"]
        img = request.FILES["img"]
        note = request.POST["note"]
        time = request.POST["timelength"]
        categorys = request.POST["category"]
        rooms = room.objects.create(
            roomname = roomname, 
            timelenght = time,
            approval = approved,
            description =note,
            address = address,
            img = img,
            admin = admin_acc.objects.get(adminid = 1),
            category = category.objects.get(id = categorys)
        )
        rooms.save()
        return redirect("/admin/")
    else :
        all_cat = category.objects.all()
        return render(request,"forms/rooms.html",{"all_cat":all_cat})

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:  # ตรวจสอบว่าเป็น admin หรือ staff
            login(request, user)
            return redirect('/admin/')  # เปลี่ยนเส้นทางไปหน้าหลักของ admin
        else:
            messages.error(request, 'Invalid credentials or unauthorized access.')
    return render(request, 'forms/login.html')