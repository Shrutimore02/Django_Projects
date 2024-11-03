from django.shortcuts import render
import  datetime
# Create your views here.
def vijaynagar_corona(request):
	data ='Corona cases in vijayngar Bangalore: 500'
	server_time=datetime.datetime.now()
	print(server_time)
	dict={'data':data, 'server_time':server_time}
	return render(request=request,template_name='bangalore/bangalore.html', context= dict)
def btm_corona(request):
	data ='Corona cases in btm Bangalore: 700'
	server_time=datetime.datetime.now()
	print(server_time)
	dict={'data':data, 'server_time':server_time}
	return render(request=request,template_name='bangalore/bangalore.html', context= dict)

def silkroad_corona(request):
	data ='Corona cases in silkroad Bangalore: 900'
	server_time=datetime.datetime.now()
	print(server_time)
	dict={'data':data, 'server_time':server_time}
	return render(request=request,template_name='bangalore/bangalore.html', context= dict)