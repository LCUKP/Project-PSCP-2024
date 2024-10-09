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
    