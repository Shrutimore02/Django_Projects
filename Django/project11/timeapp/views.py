from django.shortcuts import render
import datetime
# Create your views here.
def welcome_server_time(request):
	server_time = datetime.datetime.now()
	print(server_time)
	server_hour = int(datetime.datetime.now().hour)
	print(server_hour)
	if server_hour>0 and server_hour<12:
		msg = "Morning"
	elif server_hour>12 and server_hour<16:
		msg = "Afternoon"
	elif server_hour>16 and server_hour<21:
		msg = "Evening"
	else:
		msg = "Night"
	dict = {'server_time':server_time,'msg':msg}
	return render(request=request, template_name='timeapp/time.html', context=dict)
