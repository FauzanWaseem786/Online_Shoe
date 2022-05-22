from django.db import models

# Create your models here.


class Member(models.Model):
    Name=models.CharField(max_length =26)
    Email=models.EmailField(unique=True,default=None)
    HomeTown=models.CharField(max_length=26)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=False)
    Ingroup=models.BooleanField(default=False)
    def __str__(self):
          return self.Name

class ordr(models.Model):
    Article_num=models.CharField(max_length =200)
    sizes=models.CharField(max_length =200)
    delivery_location=models.CharField(max_length =200)
    payment_mode=models.CharField(max_length =200)
    email_id=models.EmailField(default=None,unique=False)
    phone_number=models.IntegerField()
    date=models.DateTimeField()
class Groop(models.Model):
    Name=models.CharField(max_length=200)
    Description=models.CharField(max_length=500)
    Members = models.ManyToManyField(Member)
    profil_img = models.ImageField(upload_to='profile_pics',blank=False)
