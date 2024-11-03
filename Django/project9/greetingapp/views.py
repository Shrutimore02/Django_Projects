from django.shortcuts import render
import datetime

# Create your views here.
def welcome_server_time(request):
	server_time=datetime.datetime.now()
	print(server_time)
	server_hour=int(datetime.datetime.now().hour)
	print(server_hour)
	greet=""
	if server_hour>0 and server_hour<12:
		greet="Morning"
	elif server_hour>12 and server_hour<16:
		greet="Afternoon"
	elif server_hour>16 and server_hour<21:
		greet="Evening"
	else:
		greet="Night"
	dict={'greet':greet,'server_time':server_time}
	return render(request = request, template_name='greetingapp/display.html', context=dict)
	
