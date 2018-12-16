from django.db import models
import datetime
#from django.contrib.auth.models import User
class stock(models.Model):
	itemname=models.CharField(max_length=100)
#	item_id=models.PositiveIntegerField()
	itemstock=models.PositiveIntegerField()
	itemcost=models.PositiveIntegerField()
class billdetails(models.Model):
	username=models.CharField(max_length=100)
	billnumber=models.AutoField(primary_key=True,)
	billdate=models.DateTimeField(auto_now_add=True,blank=True)
class orderdetails(models.Model):
	billnumber=models.PositiveIntegerField()
	itemname=models.CharField(max_length=100)
# Create your models here.
