from django.shortcuts import render

# Create your views here.
def display_data(request):

	return render(request=request, template_name='greetingapp/display.html')
