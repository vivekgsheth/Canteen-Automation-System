from django.db import models
from django.contrib.auth.models import User
class newuser(models.Model):
	user=models.OneToOneField(User,on_delete=models.PROTECT)
	mobileno=models.CharField(max_length=10)
# Create your models here.
