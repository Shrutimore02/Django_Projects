from django.urls import path 
from iplapp import views
urlpatterns = [
	path('homepage/', views.home_page),
	path('add/', views.add_team),
	path('list/', views.list_team),
	path('display/', views.display_teamlist),
	path('csk/', views.team_csk),
	path('dc/', views.team_dc),
	path('gt/', views.team_gt),
 	path('kkr/', views.team_kkr),
	path('lsg/', views.team_lsg),
	path('mi/', views.team_mi),
	path('pk/', views.team_pk),
	path('rcb/', views.team_rcb),
	path('rr/', views.team_rr),
	path('srh/', views.team_srh),


]