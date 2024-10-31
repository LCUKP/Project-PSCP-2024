from django.urls import path
from app_user import views

urlpatterns = [
    path('',views.index),
    path('profile',views.profile),
    path('booking',views.booking),
    path('contact',views.contact),
    path('report',views.report),
    path('register', views.register),
    path('calendar',views.calendar),
    path('login',views.login),
]