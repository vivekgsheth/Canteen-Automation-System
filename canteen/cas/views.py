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
from . models import stock
from .models import billdetails,orderdetails
from signup.models import newuser
def login(request):
	c={}
	c.update(csrf(request))
	return render(request,'login.html',c)
#@login_required
#@login_required(login_url='/ulogin/login/')
def auth_view(request):
	if request.method=="POST":
		username=request.POST.get('username','')
		password=request.POST.get('password','')
		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return HttpResponseRedirect('/cas/loggedin/')
	#else:
	return HttpResponseRedirect('/cas/login/')

#@user_passes_test(lambda u: u.is_superuser)
	
@login_required(login_url='/cas/login/')
def loggedin(request):
	items=[]
	#for i in stock.objects.all():
	#	items.append(i.itemname)
	#print(items)
	'''
	items=models.stock.objects.filter()
	'''
	items=stock.objects.values("itemname")
	print(items)
	return render(request,'cart.html', {"items":items})

@login_required(login_url='/cas/login/')
def invalidlogin(request):
	return render_to_response('invalidlogin.html')

@login_required(login_url='/cas/login/')
def logout(request):
	auth.logout(request)
	return render_to_response('welcome.html')
	
@login_required(login_url='/cas/login/')	
def choice(request):
	return render_to_response('choice.html')
	
@login_required(login_url='/cas/login/')
def previuosorder(request):
	username=request.user.username
	items=[]
	dates=[]
	pqr=billdetails.objects.all().values("username","billnumber")
	print("pqr ",pqr)
	abc=billdetails.objects.all()
	#for i in billdetails.objects.raw("select * from cas_billdetails where username= %s",[username]):
	for i in billdetails.objects.filter(username=username):
		#print(i)
		#ss=orderdetails.objects.filter(billnumber=i)
		#print("ss  ",ss)
		items.append(i.billnumber)
		#print("kk  ",items)
		dates.append(i.billdate)
		#print ("bill number is ",i.billnumber)
		#print("bill date is ",i.billdate)
	itemnames=[]
	billnumbers=[]
	details={}
	#print(items)
	flag1=0
	#i=billdetails.objects.filter(username=username).values("billnumber",flat=True)
	#print("i is ",i)	
	if items is not None:
		#print("in items not none")
		for it in items :
			flag=0
			temp=[]
		#	print(it)
		#	ss=orderdetails.objects.raw("select * from cas_orderdetails where billnumber= %s",[it])
			ss=orderdetails.objects.filter(billnumber=it)
			if ss is not None:
				#print("ss is not none ")
				for i in ss:
					if flag==0:
						billnumbers.append(it)
						details[it]=temp
						flag=1
						flag1=1
					itemnames.append(i.itemname)
					temp.append(i.itemname)
					details[it]=temp
	
		
				#print(details)
		itemnames="previous orders are "
		#return render(request,"previous.html",{"details":details,"itemnames":itemnames})
		
		
	
		if flag1==0:
			itemnames="no order till now "
			#print("no item ")
		return render(request,"previous.html",{"details":details,"itemnames":itemnames})
	

		
	

		




@login_required(login_url='/cas/login/')
def bill(request):
	if request.method=="POST":
		total=0
		now=datetime.datetime.now()
		#print("date time ",now)
		now1=datetime.datetime.now()
		now=now.strftime("%d/%m/%Y    %H:%M")
		print("now is ",now)
		now=str(now)
			
		#print(dict(request.POST)['select'])
			
		li=[]
		li2=[]
		li3=[]
		qq=0
		
		print("dict1 is ",dict(request.POST)['select'])
		print("dict2 is ",dict(request.POST)['quantity'])
		for val,val2 in zip(dict(request.POST)['select'],dict(request.POST)['quantity']):
			print("val2 is ",val2)
			if val2!=""and int(val2) >= 0:	
				print("val is ",val)
				result1=val
				#result1=val.rstrip('/')
				#print("result1 is ",result1)
				s=stock.objects.get(itemname=str(result1))
				li3.append(s.itemstock)
				li2.append(str(result1))
				if s.itemstock==0 or int(val2)>s.itemstock:
					qq=1
					li.append(s.itemname)	
					
				elif (qq != 1) :
					s.itemstock=s.itemstock-int(val2)
					s.save()
				k=s.itemcost*int(val2)
				total+=k
		if qq!=0:
			for i in range(0,len(li2)):
				s=stock.objects.get(itemname=li2[i])
				s.itemstock=li3[i]
				s.save()
		m="total is "+ str(total)
		if qq==0:
			#insert itemname
			s=billdetails(username=request.user.username,billdate=now1)
			s.save()
			bi=s.billnumber
			for i in range(0,len(li2)):
				s=orderdetails(itemname=li2[i],billnumber=bi)
				s.save()
	
		#	for i in li2:
						
			#s=billdetails()
			print("return is calling ")
			return render(request,'bill.html',{"total":total,"now":now,"items":li2})
		else :
			#items=[]
			#for i in stock.objects.raw("select * from cas_stock "):
			'''for i in stock.objects.all():
				items.append(i.itemname)'''
			print("desired")
			items=stock.objects.all().values("itemname")
			return render(request,'cart.html', {"items":items,"ina":li})
		'''else :
				#items=[]
				#for i in stock.objects.raw("select * from cas_stock "):
				#for i in stock.objects.all():
				#	items.append(i.itemname)
			items=stock.objects.all().values("itemname")	
			return render(request,'cart.html', {"items":items})'''
			
	else :
		#return HttpResponseRedirect('/cas/login/')
		items=stock.objects.all().values("itemname")
		return render(request,'cart.html',{"items":items})
def welcome(request):
	return render_to_response('welcome.html')
def gallery(request):
	return render(request,'gallery.html')

def aboutus(request):
	return render(request,'aboutus.html')
