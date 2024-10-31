from django.shortcuts import render
from app_user.models import faculty

# Create your views here.
def index(request) :
    return render(request,"adminpage.html")
def form_cat(request) :
    facultys = faculty.objects.all()
    return render(request,"forms/category.html",{"facultys":facultys})
def form_room(request) :
    if request.method == "POST" :
        name = request.POST["catname"]
        # fac = request.POST["fac"]
        print(name)
    else :
        return render(request,"forms/rooms.html")