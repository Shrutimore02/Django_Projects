from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def secondapp_res(request):
	data ='<h1> This is Response from secondapp'
	return HttpResponse(data)
