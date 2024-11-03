from django.shortcuts import render
import datetime
from django.http import HttpResponse


# Create your views here.
def welcome_server_time(request):
	msg ="welcome client"
	server_time = datetime.datetime.now()
	print(server_time)
	data = msg + '<h1>The srever time is:' + str(server_time) + '</h1>'
	return HttpResponse(data)