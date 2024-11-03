from django.shortcuts import render
from dbapp.models import StudentTable
# Create your views here.
def home_page(request):

	return render(request = request, template_name = 'dbapp/homepage.html')

def display_data(request):
	student_data = StudentTable.objects.all()
	print(student_data)
	print(type(student_data))

	my_dict = {'student_data':student_data}
	return render(request = request, template_name = 'dbapp/display.html' , context = my_dict )