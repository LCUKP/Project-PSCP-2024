from django.db import models

# Create your models here.
class user(models.Model) :
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    
    def __str__(self) :
        return  str(self.userid)+ " " + self.username + " " + self.lastname 