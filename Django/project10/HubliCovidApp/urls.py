from django.urls import path
from HubliCovidApp import views as v3

urlpatterns=[
	path('vidyanagar/',v3.vidyanagar_corona),
	path('ashwininagar/',v3.ashwininagar_corona),
	path('gokulroad/',v3.gokulroad_corona),

]