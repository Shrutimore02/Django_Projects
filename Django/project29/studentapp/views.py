from django.shortcuts import render
from studentapp.forms import StudentForm
# Create your views here.

def home_page(request):
	return render(request = request, template_name = 'studentapp/homepage.html')

def thank_you(request):
	return render(request = request, template_name = 'studentapp/thankyou.html')

def feed_back(request):
	form = StudentForm()
	my_dict = {'form':form}

	if request.method == 'POST':
		form = StudentForm(request.POST)
		my_dict = {'form':form}
		if form.is_valid():
			print("feedck from students:\n")
			print('NAME:',form.cleaned_data['name'])
			print('MAIL ID:', form.cleaned_data['mail_id'])
			print('FEEDBACK:', form.cleaned_data['feedback'])
			return thank_you(request)

	return render(request = request, template_name = 'studentapp/feedback.html', context = my_dict)

