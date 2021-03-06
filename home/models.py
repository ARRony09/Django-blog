from django.db import models
from django.http import request

# Create your models here.
class Contact(models.Model):
        sno=models.AutoField(primary_key=True)
        name=models.CharField(max_length=150)
        email=models.CharField(max_length=150)
        phone=models.CharField(max_length=20)
        content=models.TextField()
        timeStamp=models.DateTimeField(auto_now_add=True,blank=True)

        def __str__(self):
            return "Message from " + self.name + ' - ' + self.email
        

class Author(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField()