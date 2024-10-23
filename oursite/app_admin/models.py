from django.db import models

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
    
    def __str__(self) :
        return  str(self.position)+ " " + self.name
    
class category(models.Model) :
    catname = models.CharField(max_length=200)
    permission = models.CharField(max_length=255)
    img = models.ImageField(upload_to ='app_admin/static/img/cat/')
    admin = models.ForeignKey(admin_acc,on_delete=models.CASCADE)
    
    def __str__(self) :
        return  str(self.catid)+ " " + self.catname
    
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
        return  str(self.roomid)+ " " + self.roomname