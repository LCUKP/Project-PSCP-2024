from django.db import models
from app_admin.models import room
from django.utils import timezone

# # Create your models here.
class faculty(models.Model) :
    facid = models.AutoField(primary_key=True)
    facname = models.CharField(max_length=200)

    def __str__(self) :
        return  str(self.facid)+ " " + self.facname
    
class major(models.Model) :
    majorname = models.CharField(max_length=200)
    facid = models.ForeignKey(faculty,on_delete=models.CASCADE)
    
    def __str__(self) :
        return  self.majorname

class user(models.Model) :
    code = models.CharField(max_length=13)
    username = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    img = models.ImageField(upload_to ='app_user/static/img/')
    faculty = models.ForeignKey(faculty,on_delete=models.CASCADE)
    major = models.ForeignKey(major,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)  # เพิ่ม is_active ที่ต้องการ
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(default=timezone.now)  # เพิ่มฟิลด์ last_login
    date_joined = models.DateTimeField(default=timezone.now)  # ฟิลด์ที่บันทึกเวลาที่ผู้ใช้สมัคร

    @property
    def is_authenticated(self):
        # ฟังก์ชันนี้จะคืนค่าความเป็นจริง (True) ถ้าผู้ใช้ล็อกอินอยู่
        return True  # ในกรณีนี้สมมุติว่าเป็นผู้ใช้ที่ได้รับการยืนยันเสมอ
    
    def __str__(self) :
        return  self.code + " " + self.name + " " + self.lastname
    
class booking(models.Model) :
    datebook = models.CharField(max_length=200,null=False)
    timebook = models.CharField(max_length=200,null=False)
    reason = models.CharField(max_length=200,null=True)
    user = models.ManyToManyField(user)
    room = models.ManyToManyField(room)
    
    def __str__(self) :
        return  str(self.datebook)+ " " + self.timebook 