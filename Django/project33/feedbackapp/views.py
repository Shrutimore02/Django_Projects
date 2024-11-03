from django.shortcuts import render
from feedbackapp.forms import StudentForm
# Create your views here.
def home_page(request):
	return render(request = request, template_name = 'feedbackapp/homepage.html')

def thank_you(request):
	return render(request = request, template_name = 'feedbackapp/thankyou.html')

def feed_back(request):

	form = StudentForm()
	my_dict = {'form':form}

	if request.method == 'POST':
		form = StudentForm(request.POST)
		my_dict = {'form':form}
		if form.is_valid():
			print("the feedback enterd by the student is :\n")
			print('NAME:',form.cleaned_data['name'])
			print('MAIL ID:', form.cleaned_data['mail_id'])
			print('PASSWORD:', form.cleaned_data['password'])
			print('FEEDBACK:', form.cleaned_data['feedback'])
			print('BOT HANDLER:', form.cleaned_data['bot_handler'])


			return thank_you(request)

	return render(request = request, template_name = 'feedbackapp/feedback.html', context = my_dict)
