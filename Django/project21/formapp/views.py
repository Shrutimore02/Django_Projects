from django.shortcuts import render
from formapp.forms import Cricketer
# Create your views here.
def cricketer_data(request):
	cricketer_data = Cricketer()
	my_dict = {'cricketer_data':cricketer_data}
	return render(request = request, template_name = 'formapp/display.html', context = my_dict)
