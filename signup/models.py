from django.db import models

# Create your models here.
class signupdata(models.Model):
    name=models.CharField(max_length=50)
    phone=models.BigIntegerField(unique=True)
    email=models.EmailField(max_length=50,unique=True)
    gender=models.CharField(max_length=5)
    active=models.CharField(default=False,max_length=7)
    password=models.CharField(max_length=10)
    otp=models.IntegerField(default=0)