from django.utils import timezone
from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class admin_acc(models.Model) :
    adminid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    contact = models.URLField(max_length=200)
    phone = models.URLField(max_length=20)
    img = models.ImageField(upload_to ='app_admin/static/img/')

    is_active = models.BooleanField(default=True)  # เพิ่ม is_active ที่ต้องการ
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(default=timezone.now)  # เพิ่มฟิลด์ last_login
    date_joined = models.DateTimeField(default=timezone.now)  # ฟิลด์ที่บันทึกเวลาที่ผู้ใช้สมัคร

    def save(self, *args, **kwargs):
        # ตรวจสอบว่า password ได้รับการเข้ารหัสแล้วหรือยัง
        if not self.password.startswith('pbkdf2_'):  # เช็คว่ารหัสผ่านถูก hash หรือยัง
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    @property
    def is_authenticated(self):
        # ฟังก์ชันนี้จะคืนค่าความเป็นจริง (True) ถ้าผู้ใช้ล็อกอินอยู่
        return True  # ในกรณีนี้สมมุติว่าเป็นผู้ใช้ที่ได้รับการยืนยันเสมอ
    
    def __str__(self) :
        return  str(self.position)+ " " + self.name
    
class category(models.Model) :
    catname = models.CharField(max_length=200)
    permission = models.CharField(max_length=255)
    address = models.CharField(max_length=255, default="Invalid")
    time = models.CharField(max_length=100, default="08:00-20:00")
    note = models.CharField(max_length=255, default="Invalid")
    img = models.ImageField(upload_to ='app_admin/static/img/cat/')
    admin = models.ForeignKey(admin_acc,on_delete=models.CASCADE)
    
    def __str__(self) :
        return  str(self.id)+ " " + self.catname
    
class room(models.Model) :
    roomname = models.CharField(max_length=200)
    timelenght = models.IntegerField()
    approval = models.BooleanField(default=False)
    description = models.TextField()
    address = models.CharField(max_length=200)
    img = models.ImageField(upload_to ='app_admin/static/img/rooms/')
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    admin = models.ForeignKey(admin_acc,on_delete=models.CASCADE)
    
    def __str__(self) :
        return  str(self.id)+ " " + self.roomname