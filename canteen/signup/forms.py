from django import forms
from .models import newuser
from django.contrib.auth.models import User
class userForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model=User
		fields=("username","password","email")

class newuserForm(forms.ModelForm):
	class Meta:
		model=newuser
		fields=("mobileno",)
	