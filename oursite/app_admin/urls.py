from django.urls import path
from app_admin import views

urlpatterns = [
    path("",views.index)
]