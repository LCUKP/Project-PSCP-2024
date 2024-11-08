from django.urls import path,include
from app_admin import views

urlpatterns = [
    path("",views.index),
    path("login", views.admin_login),
    path("logout", views.logouts),
    path("add-category",views.form_cat),
    path("add-room",views.form_room),
    path("manage-room",views.admin_manage),
    path("history",views.history),
    path("profile",views.adminprofile)
]