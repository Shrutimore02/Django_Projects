from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display_data(request):
	data="<h1>welcome to learn django and REST API</h1>"
	return	HttpResponse(data)

