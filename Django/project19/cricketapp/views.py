from django.shortcuts import render
from cricketapp.models import CricketData
# Create your views here.
def home_page(request):
	return render(request = request, template_name = 'cricketapp/homepage.html')


def display(request):
	cricketer_data = CricketData.objects.all()
	my_dict = {'cricketer_data':cricketer_data}
	return render(request = request, template_name = 'cricketapp/display.html', context = my_dict)
