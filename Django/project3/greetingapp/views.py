from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.
def welcome_server_time(request):
	msg = '<h1>Hii Client Good'
	#The below logic is to fetch the current server time 
	server_time = datetime.datetime.now()
	print(server_time)
	print(type(server_time))

	#The below logic is to fetch the current server hour 
	server_hour = int(datetime.datetime.now().hour)

	if server_hour>0 and server_hour<12:
		msg = msg +' Morning'
	elif server_hour>12 and server_hour<16:
		msg = msg +' Afternoon'
	elif server_hour>16 and server_hour<21:
		msg = msg +' Evening'
	else:
		msg=msg + ' Night'

	msg= msg + '</h1><hr>'
	data = msg + ' The server time is:' + str(server_time)
	return HttpResponse(data)
