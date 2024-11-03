from django.shortcuts import render
from studentapp.models import StudentTable
from studentapp.forms import StudentTableForm
# Create your views here.
def home_page(request):
	return render(request = request, template_name = 'studentapp/homepage.html')



def add_data(request):
	student_form = StudentTableForm()
	my_dict = {'student_form':student_form}
	if request.method == 'POST':
		student_form = StudentTableForm(request.POST)
		if student_form.is_valid():
			student_form.save(commit = True)

			print("Details Entered by the Student:\n")
			print('NAME:',student_form.cleaned_data['name'])
			print('ROLL NO.:', student_form.cleaned_data['roll_no'])
			print('SUBJECT:',student_form.cleaned_data['subject'])
			print('MARKS:',student_form.cleaned_data['marks'])
	return render(request = request, template_name = 'studentapp/add.html',context = my_dict)


def list_data(request):
	student_data = StudentTable.objects.all()
	data_dict = {'student_data':student_data}
	return render(request = request, template_name = 'studentapp/list.html', context = data_dict)

