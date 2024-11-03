from django.shortcuts import render
from modelformapp.models import StudentTable
from modelformapp.forms import StudentTableForm
# Create your views here.
def student_data(request):
	form = StudentTableForm()
	my_dict = {'form':form}

	if request.method == 'POST':
		form = StudentTableForm(request.POST)
		
		if form.is_valid():
			form.save(commit = True)
			print("Data is sucessfully stired in Database\n\n")
			print("the data is entered by student is:\n")
			print('NAME:', form.cleaned_data['name'])
			print('DOB:', form.cleaned_data['dob'])
			print('MAIL ID:', form.cleaned_data['mail_id'])
			print('PHONE NUMBER:', form.cleaned_data['phone_number'])
			print('BRANCH:', form.cleaned_data['branch'])
	return render(request = request, template_name = 'modelformapp/display.html', context = my_dict)

