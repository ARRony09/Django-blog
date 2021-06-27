from django.db import models
from django.http import request

# Create your models here.
class Post(models.Model):
        sno=models.AutoField(primary_key=True)
        title=models.CharField(max_length=150)
        author=models.CharField(max_length=200)
        slug=models.CharField(max_length=200)
        content=models.TextField()
        image=models.ImageField(upload_to='blog/image',default='')
        timeStamp=models.DateTimeField(blank=True)

        def __str__(self):
            return self.title + ' by ' + self.author

from django.contrib.auth.models import User
from django.utils.timezone import now

class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)
        

