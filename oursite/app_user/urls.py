from django.urls import path,include
from app_user import views

urlpatterns = [
    path('',views.index),
    path('login', views.user_login),
    path('logout', views.user_logout),
    path('profile',views.profile),
    path('booking',views.booking_view),
    path('contact',views.contact),
    path('report',views.report),
    path('register', views.register),
    path('calendar',views.calendar_view),
    path('time',views.time),
    path('test_register', views.test_register),
    path('test', views.test),
    path('reservation',views.reservation),
    path('selectroom',views.selectroom)
]