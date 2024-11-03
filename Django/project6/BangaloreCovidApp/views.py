from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vijaynagar_corona(request):
	data ='<h1> Corona cases in vijayngar Bangalore: 500</h1>'
	return HttpResponse(data)

def btm_corona(request):
	data ='<h1> Corona cases in btm Bangalore: 700</h1>'
	return HttpResponse(data)

def silkroad_corona(request):
	data ='<h1> Corona cases in silkroad Bangalore: 900</h1>'
	return HttpResponse(data)
