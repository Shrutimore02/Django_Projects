from django.shortcuts import render

# Create your views here.
def degree(request):
	msg = "My name is Shruti, Basically im from Nashik Below is my Degree Certificate"
	dict = {'msg':msg}
	return render(request = request, template_name = 'degreeapp/degree.html', context = dict)