"""
URL configuration for project5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BangaloreCovidApp import views as v1
from MysoreCovidApp import views as v2
from HubliCovidApp import views as v3


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bangalore/vijaynagar', v1.vijaynagar_corona),
    path('bangalore/btm', v1.btm_corona),
    path('bangalore/silkroad', v1.silkroad_corona),

    path('mysore/rknagar', v2.rknagar_corona),
    path('mysore/vijaynagar', v2.vijaynagar_corona),
    path('mysore/KDroad', v2.KDroad_corona),

    path('hubli/vidyanagar', v3.vidyanagar_corona),
    path('hubli/ashwininagar', v3.ashwininagar_corona),
    path('hubli/gokulroad', v3.gokulroad_corona),


]
