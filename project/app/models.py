from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone=models.IntegerField()
    desc=models.TextField(max_length=300)

    def __int__(self):
        return self.phone
    
class BlogPost(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    content=models.TextField()
    name=models.CharField(max_length=25)
    timeStamp = models.DateTimeField(blank=True)

    def __int__(self):
        return self.sno
    



