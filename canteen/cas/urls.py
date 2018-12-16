from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from .views import login,auth_view,previuosorder,logout,loggedin,invalidlogin,choice,bill
urlpatterns = [
	url(r'^login/$', login,name='user_login'),	
	url(r'^auth/$', auth_view),	
	url(r'^logout/$', logout),
	url(r'^loggedin/$', loggedin),
	url(r'^invalidlogin/$', invalidlogin),
	#url(r'^register/$',userregisteration),
	url(r'^choice/$',choice),
	url(r'^bill/$',bill),
	url(r'^previous/$',previuosorder),
	
]

