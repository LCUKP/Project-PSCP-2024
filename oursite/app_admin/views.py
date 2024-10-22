from django.shortcuts import render

# Create your views here.
def index(request) :
    return render(request,"adminpage.html") 
def form_cat(request) :
    return render(request,"forms/category.html")
def form_room(request) :
    return render(request,"forms/rooms.html")