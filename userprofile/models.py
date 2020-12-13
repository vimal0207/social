from django.db import models
from picklefield.fields import PickledObjectField

# Create your models here.
class frienddetail(models.Model):
    id=models.BigIntegerField(primary_key=True)
    friendlist=PickledObjectField()
    friendrequest=PickledObjectField()
    friendrequestsend=PickledObjectField()

class post(models.Model):
    userid=models.BigIntegerField()
    name=models.CharField(max_length=500)
    article=PickledObjectField()
    image=PickledObjectField()
    