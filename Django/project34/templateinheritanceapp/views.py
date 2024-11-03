from django.shortcuts import render

# Create your views here.

def homepage_info(request):
	return render(request = request, template_name = 'templateinheritanceapp/homepage.html')

def movies_info(request):
	return render(request = request, template_name = 'templateinheritanceapp/movies.html')

def events_info(request):
	return render(request = request, template_name = 'templateinheritanceapp/events.html')

def sports_info(request):
	return render(request = request, template_name = 'templateinheritanceapp/sports.html')

