from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def firstapp_res(request):
	data= '<h1> This is Response from firstapp</h1>'
	return HttpResponse(data)
