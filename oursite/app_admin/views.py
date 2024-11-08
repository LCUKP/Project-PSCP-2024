from django.shortcuts import render,redirect
from app_user.models import faculty, booking
from app_admin.models import room, admin_acc, category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Count

# Create your views here.
def index(request) :
    return render(request,"adminpage.html")
def admin_manage(request) :
    adminid = request.user.adminid
    cat = category.objects.filter(admin = adminid).annotate(room_count=Count('room'))
    rooms = room.objects.filter(admin = adminid)
    return render(request,"admin_manager.html",{"cat":cat,"room":rooms})
def history(request) :
    adminid = request.user.adminid
    books = booking.objects.filter(room = adminid)
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
        adminid = request.user.adminid
        cat = category.objects.create(
            catname = catname,
            permission = fac,
            img = img,
            admin = admin_acc.objects.get(adminid = adminid),
            address = address,
            time = time,
            note = note,
        )
        cat.save()
        return redirect("/admin/manage-room")
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
        adminid = request.user.adminid
        rooms = room.objects.create(
            roomname = roomname, 
            timelenght = time,
            approval = approved,
            description =note,
            address = address,
            img = img,
            admin = admin_acc.objects.get(adminid = adminid),
            category = category.objects.get(id = categorys)
        )
        rooms.save()
        return redirect("/admin/manage-room")
    else :
        adminid = request.user.adminid
        all_cat = category.objects.filter(admin = adminid)
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
    return render(request, 'adminpage.html')

def logouts(request):
    logout(request)  # ล็อกเอาท์ผู้ใช้
    return redirect('/admin/')

def adminprofile(request):
    return render(request, 'adminprofile.html')