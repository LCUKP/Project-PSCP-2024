from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import user as User  # นำเข้า User ที่ถูกต้อง
from app_admin.models import admin_acc as Admin  # นำเข้าตาราง `admin` ที่กำหนดเอง

class UserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)  # ใช้ user (พิมพ์เล็ก) แทน User (พิมพ์ใหญ่)
            if check_password(password, user.password):  # ตรวจสอบรหัสผ่านที่เข้ารหัส
                print(111)
                return user
            else :
                print(333)
        except User.DoesNotExist:
            print(222)
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class AdminBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            admin = Admin.objects.get(username=username)
            if check_password(password, admin.password):  # ตรวจสอบรหัสผ่าน
                return admin
        except Admin.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Admin.objects.get(pk=user_id)
        except Admin.DoesNotExist:
            return None