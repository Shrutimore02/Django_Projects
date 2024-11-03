from django.shortcuts import render
import datetime
# Create your views here.
def vidyanagar_corona(request):
	data ='Corona cases in vidyanagar Hubli: 350'
	server_time=datetime.datetime.now()
	print(server_time)
	dict={'data':data, 'server_time':server_time}
	return render(request=request,template_name='hubli/hubli.html', context= dict)

def ashwininagar_corona(request):
	data ='Corona cases in ashwininagar Hubli: 500'
	server_time=datetime.datetime.now()
	print(server_time)
	dict={'data':data, 'server_time':server_time}
	return render(request=request,template_name='hubli/hubli.html', context= dict)

def gokulroad_corona(request):
	data ='Corona cases in gokulroad Hubli: 840'
	server_time=datetime.datetime.now()
	print(server_time)
	dict={'data':data, 'server_time':server_time}
	return render(request=request,template_name='hubli/hubli.html', context= dict)
