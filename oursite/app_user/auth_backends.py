# auth_backends.py
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import user as User  # นำเข้า User ที่ถูกต้อง

class UserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)  # ใช้ user (พิมพ์เล็ก) แทน User (พิมพ์ใหญ่)
            if check_password(password, user.password):  # ตรวจสอบรหัสผ่านที่เข้ารหัส
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None