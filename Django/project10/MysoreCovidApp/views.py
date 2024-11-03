from django.shortcuts import render
import datetime
# Create your views here.
def rknagar_corona(request):
	data ='Corona cases in vijayngar Mysore: 570'
	server_time=datetime.datetime.now()
	print(server_time)
	dict={'data':data, 'server_time':server_time}
	return render(request=request,template_name='mysore/mysore.html', context= dict)

def vijaynagar_corona(request):
	data ='Corona cases in vijayngar Mysore: 200'
	server_time=datetime.datetime.now()
	print(server_time)
	dict={'data':data, 'server_time':server_time}
	return render(request=request,template_name='mysore/mysore.html', context= dict)

def KDroad_corona(request):
	data ='Corona cases in KDroad Mysore: 456'
	server_time=datetime.datetime.now()
	print(server_time)
	dict={'data':data, 'server_time':server_time}
	return render(request=request,template_name='mysore/mysore.html', context= dict)

