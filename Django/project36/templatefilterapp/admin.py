from django.contrib import admin
from templatefilterapp.models import FilterModel
# Register your models here.
class FilterModelAdmin(admin.ModelAdmin):
	list_display = ['id','name','age','iplteam']
admin.site.register(FilterModel, FilterModelAdmin)