from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def thirdapp_res(request):
	data='<h1>This is Response from thirdapp'
	return HttpResponse(data)
