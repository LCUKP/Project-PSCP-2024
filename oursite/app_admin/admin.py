from django.contrib import admin
from app_admin.models import admin as admin_user,room,category

# Register your models here.
admin.site.register(admin_user)
admin.site.register(room)
admin.site.register(category)

