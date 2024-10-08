from django.shortcuts import render
from django.http import HttpResponse
from app_user.models import user

# Create your views here.
def index(request) :
    all_user = user.objects.all()
    user2 = user.objects.filter(userid = 2)
    return render(request,"index.html",{"all_user":all_user,"user2":user2})
