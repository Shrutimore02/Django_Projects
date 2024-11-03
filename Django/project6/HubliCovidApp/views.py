from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vidyanagar_corona(request):
	data ='<h1> Corona cases in vidyanagar Hubli: 350</h1>'
	return HttpResponse(data)

def ashwininagar_corona(request):
	data ='<h1> Corona cases in ashwininagar Hubli: 500</h1>'
	return HttpResponse(data)

def gokulroad_corona(request):
	data ='<h1> Corona cases in gokulroad Hubli: 840</h1>'
	return HttpResponse(data)