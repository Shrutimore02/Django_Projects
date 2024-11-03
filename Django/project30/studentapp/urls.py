from django.urls import path  
from studentapp import views

urlpatterns = [
	path('homepage/', views.home_page),
	path('feedback/', views.feed_back),
	path('thankyou/', views.thank_you),
]