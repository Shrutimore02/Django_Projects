from django.shortcuts import render
from formapp.forms import StudentForm
# Create your views here.
def home_page(request):
	return render(request = request, template_name = 'formapp/homepage.html')

def register(request):
	if request.method =='GET':
		form = StudentForm()
		my_dict = {'form':form}
		return render(request = request, template_name = 'formapp/register.html', context = my_dict)

	if request.method =='POST':
		form = StudentForm(request.POST)
		my_dict = {'form':form}

		if form.is_valid():
			print("The Details Entred by the SAtudent:\n\n")
			print('NAME:',form.cleaned_data['name'])
			print('PASSWORD:',form.cleaned_data['password'])
			print('AGAIN PASSWORD:',form.cleaned_data['re_password'])
			print('TRAINER:',form.cleaned_data['trainer_name'])
			print('SUBJECT:',form.cleaned_data['subject'])
			print('DATE:',form.cleaned_data['date'])
			print('MAIL ID:',form.cleaned_data['mail_id'])
			print('PHONE NUMBER:',form.cleaned_data['phone_number'])
			print('FEEDBACK:',form.cleaned_data['feedback'])
		return render(request = request, template_name = 'formapp/register.html', context = my_dict)