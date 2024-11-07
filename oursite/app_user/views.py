import calendar, datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app_user.models import user,faculty,major
from app_admin.models import admin_acc,category, room

# Create your views here.
def index(request) :
    if request.user.is_authenticated :
        all_category = category.objects.all()
        return render(request,"index.html",{"all_category":all_category})
    return render(request,"index.html")

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
            password = password,
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
    lenght = [f"{i:0>2}" for i in range(int(time[0][:2]),int(time[1][:2])+1,1)]
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