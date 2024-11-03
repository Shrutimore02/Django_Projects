from django.urls import path
from BangaloreCovidApp import views as v1

urlpatterns=[
	path('vijaynagar/',v1.vijaynagar_corona),
	path('btm/',v1.btm_corona),
	path('silkroad/',v1.silkroad_corona),

	
]