from django.urls import path,include
from app_admin import views

urlpatterns = [
    path("",views.index),
    path("login", views.admin_login),
    path("add-category",views.form_cat),
    path("add-room",views.form_room),
    path("manage-room",views.admin_manage)
]