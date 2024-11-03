from django.shortcuts import render

# Create your views here.
def home_page(request):
	return render(request=request, template_name='ndtvapp/homepage.html')

def display_movies_information(request):
	main_msg = 'Latest Movies Infromation'

	msg1 = 'RRR shooting is in progress!!!'
	msg2 = 'Robert by dboss has been released this year'

	my_dict = {'main_msg':main_msg,'msg1':msg1,'msg2':msg2}
	return render(request = request, template_name = 'ndtvapp/movies.html', context = my_dict)

def display_sports_information(request):
	main_msg = 'Latest Sports Infromation'

	msg1 = 'IPL will be held in India'
	msg2 = 'Dhoni got retired from Indian Cricket Team'

	my_dict = {'main_msg':main_msg,'msg1':msg1,'msg2':msg2}
	return render(request = request, template_name = 'ndtvapp/sports.html', context = my_dict)

def display_politics_information(request):
	main_msg = 'Latest Politics Infromation'

	msg1 = 'Modi will become PM for next elections also!!!'
	msg2 = 'Rahul Gandhi is best bachelor in Indian'

	my_dict = {'main_msg':main_msg,'msg1':msg1,'msg2':msg2}
	return render(request = request, template_name = 'ndtvapp/politics.html', context = my_dict)
