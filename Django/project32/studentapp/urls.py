from django.urls import path  
from studentapp import views

urlpatterns = [
	path('homepage/', views.home_page),
	path('thankyou/', views.thank_you),
	path('feedback/', views.feed_back),
]