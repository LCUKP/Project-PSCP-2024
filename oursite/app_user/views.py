import calendar, datetime
from pyexpat.errors import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app_user.models import user,faculty,major,booking
from app_admin.models import admin_acc,category, room
from django.contrib.auth.hashers import make_password


# Create your views here.
def index(request) :
    if request.user.is_authenticated :
        all_category = category.objects.all()
        return render(request,"index.html",{"all_category":all_category})
    return render(request,"index.html")

def profile(request) :
    return render(request,"profile.html")

@login_required
def booking_view(request) :
    if request.method == "POST":
        times = request.POST.getlist('time')
        time = f"{times[0]}-{times[-1]}"
        catid = request.GET.get("catid")
        roomb = request.GET.get("roomid")
        roomid = request.GET.get("roomid")
        userid = request.user.id
        date = "{} {} {} {}".format(
            request.GET.get("day"),
            request.GET.get("date"),
            request.GET.get("month"),
            int(request.GET.get("years")) + 543
        )
        book = booking.objects.create(
            datebook = date,
            timebook = time,
            reason = "Invalidation",
        )
        cat = category.objects.get(id = catid)
        users = user.objects.get(id=userid)
        rooms = room.objects.get(id=roomb)
        book.user.set([users])
        book.room.set([rooms])
        book.save()
    return render(request,"booking.html",{"date":date,"time":time,"cat":cat,"room":rooms})

def contact(request) :
    admins = admin_acc.objects.all()
    return render(request,"contact.html",{"admins":admins})

def report(request) :
    return render(request,"report.html")

def register(request) :
    if request.method == "POST":
        username = request.POST["username"]
        studentid = request.POST["code"]
        name = request.POST["name"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        facultys = request.POST["faculty"]
        img = request.FILES["img"]
        majors = request.POST["major"]
        User = user.objects.create(
            code = studentid,
            username = username,
            name = name,
            lastname = lastname,
            password = make_password(password),
            faculty = faculty.objects.get(facid=facultys),
            img = img,
            major = major.objects.get(id=majors),
        )
        User.save()
        return redirect('/#popup')
    all_faculty = faculty.objects.all()
    all_major = major.objects.all()
    return render(request,"forms/register.html",{"all_faculty":all_faculty,"all_major":all_major})

def calendar_view(request) :
    catid = request.GET.get("catid")
    roomid = request.GET.get("roomid")
    year = int(datetime.datetime.now().strftime("%Y"))
    month = int(datetime.datetime.now().strftime("%m"))
    months_thai = ["มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"]
    if request.method == "POST":
        data = request.POST.get("data")
        data_month = (months_thai.index(request.POST.get("month")))+1
        if data == "p" :
            data_month  += 1
            if data_month > 12 :
                data_month = 1
                year += 1
            month = data_month
            print("ppp",month)
        elif data == "s" :
            if data_month > int(datetime.datetime.now().strftime("%m")) :
                data_month  -= 1
            month = data_month
            print("sss",month)
    months = int(datetime.datetime(year, month, 1).strftime("%m"))-1
    years = int(datetime.datetime(year, month, 1).strftime("%Y"))+543
    month_days = calendar.monthcalendar(year, month)
    dates = [week for week in month_days]
    return render(request,"forms/calendar.html",{"dates":dates,"month":months_thai[months],"years":years,"months_thai":months_thai,"catid":catid,"roomid":roomid})

def login(request) :
    pass

def time(request):
    months_thai = ["มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"]
    days_in_thai = ["อาทิตย์", "จันทร์", "อังคาร", "พุธ", "พฤหัสบดี", "ศุกร์", "เสาร์"]
    catid = request.GET.get("catid")
    roomid = request.GET.get("roomid")
    date = int(request.GET.get("date"))
    cat = category.objects.get(id = catid)
    rooms = room.objects.get(id = roomid)
    time = (category.objects.get(id = catid).time).split("-")
    lenght = [(f"{i:0>2}",f"{i+1:0>2}") for i in range(int(time[0][:2]),int(time[1][:2])+1,1)]
    print(lenght)
    month = months_thai.index(request.GET.get("month"))
    years = int(request.GET.get("years"))-543
    day = int(datetime.datetime(years,month,date).strftime("%w"))
    # print(date,month,years,catid,roomid)
    return render(request,"forms/time.html",{"date":date,"month":months_thai[month],"years":years,"day":days_in_thai[day],"cat":cat,"room":rooms,"lenght":lenght})

def test(request) :
    return render(request,"forms/test.html")

def test_register(request):
    if request.method == 'POST':
        return HttpResponse("Received POST request!")
    elif request.method == 'GET':
        return HttpResponse("Not a POST request")

def reservation(request):
    return render(request,"forms/reservation.html")

def selectroom(request):
    catid = request.GET.get("catid")
    all_room = room.objects.filter(id = catid)
    return render(request,"forms/selectroom.html",{"all_room":all_room})

# def custom_login_view(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.error(request, "Invalid username or password")
#     return render(request, 'login.html')