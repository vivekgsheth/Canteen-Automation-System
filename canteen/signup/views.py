from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test
import datetime
#from . models import stock
from . import forms
from .models import newuser
def userregisteration(request):
		if request.method=="POST":
			form1=forms.userForm(request.POST)
			form2=forms.newuserForm(request.POST)
			if form1.is_valid and form2.is_valid:
				user=form1.save()
				user.set_password(user.password)
				user.save()
				reg=form2.save(commit=False)
				reg.user=user
				reg.save()
				return HttpResponseRedirect('/cas/login/')
		else :
			form1=forms.userForm()
			form2=forms.newuserForm()
			args={'form1':form1,'form2':form2}
		
		return render(request,'register.html',args)

# Create your views here.
