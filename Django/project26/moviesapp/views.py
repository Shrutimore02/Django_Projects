from django.shortcuts import render
from moviesapp.models import MovieTable
from moviesapp.forms import MovieTableForm
# Create your views here.
def home_page(request):
	return render(request = request, template_name = 'moviesapp/homepage.html')


def add_movie(request):
	movie_form = MovieTableForm()
	my_dict = {'movie_form':movie_form}

	if request.method == 'POST':
		movie_form = MovieTableForm(request.POST)
		if movie_form.is_valid():
			movie_form.save(commit = True)

	
			print("details of movie is:\n")
			
			print('NAME OF MOVIE:',movie_form.cleaned_data['movie_name'])
			print('HERO:',movie_form.cleaned_data['hero'])
			print('HEROINE:',movie_form.cleaned_data['heroine'])

	return render(request = request, template_name = 'moviesapp/add.html', context = my_dict)


def movie_list(request):
	movies = MovieTable.objects.all()
	list_dict = {'movies':movies}
	return render(request = request, template_name = 'moviesapp/list.html', context = list_dict)


