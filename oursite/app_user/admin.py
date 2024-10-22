from django.contrib import admin
from app_user.models import user,booking,faculty,major

# Register your models here.
admin.site.register(user)
admin.site.register(booking)
admin.site.register(faculty)
admin.site.register(major)
