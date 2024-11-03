from django.urls import path 
from studentapp import views

urlpatterns = [
	path('homepage/',views.home_page),
	path('add/', views.add_data),
	path('list/', views.list_data),
]