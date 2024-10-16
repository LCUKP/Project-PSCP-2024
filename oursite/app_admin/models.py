from django.db import models

# Create your models here.
class admin(models.Model) :
    adminid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    contact = models.URLField(max_length=200)
    img = models.ImageField(upload_to ='app_admin/static/img/')
    
    def __str__(self) :
        return  str(self.position)+ " " + self.name
    
class category(models.Model) :
    catid = models.AutoField(primary_key=True)
    catname = models.CharField(max_length=200)
    permission = models.BooleanField(default=False)
    
    def __str__(self) :
        return  str(self.catid)+ " " + self.catname
    
class room(models.Model) :
    roomid = models.AutoField(primary_key=True)
    roomname = models.CharField(max_length=200)
    timelenght = models.IntegerField(max_length=2)
    approval = models.BooleanField(default=False)
    description = models.TextField()
    address = models.CharField(max_length=200)
    room_img = models.ImageField(upload_to ='app_admin/static/img/rooms/')
    # catid = models.ForeignKey(category,on_delete=models.CASCADE)
    adminid = models.ForeignKey(admin,on_delete=models.CASCADE)
    
    def __str__(self) :
        return  str(self.roomid)+ " " + self.roomname