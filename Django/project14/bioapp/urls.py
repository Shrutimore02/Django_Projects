from django.urls import  path
from bioapp import views
urlpatterns = [
	path('home/',views.display_biodata),
	path('sslc/',views.display_sslc),
	path('puc/',views.display_puc),
	path('degree/',views.display_degree),


]