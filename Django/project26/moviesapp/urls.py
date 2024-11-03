from django.urls import path 
from moviesapp import views
urlpatterns = [
	path('homepage/', views.home_page),
	path('add/', views.add_movie),
	path('list/', views.movie_list),
]