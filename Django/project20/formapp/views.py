from django.shortcuts import render
from formapp.forms import Student
# Create your views here.
def student_data(request):
	student_data = Student()
	my_dict = {'student_data':student_data}
	return render(request = request, template_name = 'formapp/display.html', context = my_dict)
