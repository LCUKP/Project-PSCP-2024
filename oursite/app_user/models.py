from django.db import models
from app_admin.models import room

# Create your models here.
class user(models.Model) :
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    
    def __str__(self) :
        return  str(self.userid)+ " " + self.username + " " + self.lastname
    
class booking(models.Model) :
    bookid = models.AutoField(primary_key=True)
    datebook = models.DateField(null=False)
    timebook = models.TimeField(null=False)
    userid = models.ForeignKey(user,on_delete=models.CASCADE)
    roomid = models.ForeignKey(room,on_delete=models.CASCADE)
    
    def __str__(self) :
        return  str(self.bookid)+ " " + self.roomid + " " + self.datebook 

class faculty(models.Model) :
    facid = models.AutoField(primary_key=True)
    facname = models.CharField(max_length=200)
    
    def __str__(self) :
        return  str(self.facid)+ " " + self.facname