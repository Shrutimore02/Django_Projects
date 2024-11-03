from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def rknagar_corona(request):
	data ='<h1> Corona cases in vijayngar Mysore: 570</h1>'
	return HttpResponse(data)

def vijaynagar_corona(request):
	data ='<h1> Corona cases in vijayngar Mysore: 200</h1>'
	return HttpResponse(data)

def KDroad_corona(request):
	data ='<h1> Corona cases in KDroad Mysore: 456/h1>'
	return HttpResponse(data)

