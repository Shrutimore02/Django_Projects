from django.contrib import admin
from customfilterapp.models import UserTemplateFilter
# Register your models here.
class UserTemplateFilterAdmin(admin.ModelAdmin):

	list_display = ['name', 'technology','trainer']
	
admin.site.register(UserTemplateFilter,UserTemplateFilterAdmin)
