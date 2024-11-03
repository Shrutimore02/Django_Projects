from django import forms 
from moviesapp.models import MovieTable
class MovieTableForm(forms.ModelForm):
    class Meta:
        model = MovieTable
        fields = ('id', 'movie_name','hero', 'heroine')
