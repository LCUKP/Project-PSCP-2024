from django.db import models
from app_admin.models import room

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
    
    def __str__(self) :
        return  self.code + " " + self.name + " " + self.lastname
    
class booking(models.Model) :
    datebook = models.DateField(null=False)
    timebook = models.TimeField(null=False)
    reason = models.CharField(max_length=200,null=True)
    user = models.ManyToManyField(user)
    room = models.ManyToManyField(room)
    
    def __str__(self) :
        return  str(self.bookid)+ " " + self.roomid + " " + self.datebook 