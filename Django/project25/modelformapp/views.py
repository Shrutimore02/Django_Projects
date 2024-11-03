from django.shortcuts import render
from modelformapp.models import EmployeeData
from modelformapp.forms import EmployeeDataForm
# Create your views here.
def employee_data(request):
	form = EmployeeDataForm()
	my_dict = {'form':form}

	if request.method == 'POST':
		form = EmployeeDataForm(request.POST)
		form.save(commit = True)
		if form.is_valid():
			print("Data is sucessfully stored in the MYSQL Database\n\n")
			print('The data entered by Employee is:\n')
			print('NAME:', form.cleaned_data['name'])
			print('JOB:', form.cleaned_data['job'])
			print('SALARY:', form.cleaned_data['salary'])
	return render(request = request, template_name = 'modelformapp/display.html', context = my_dict)


			