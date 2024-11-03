from django.contrib import admin
from dbapp.models import Cricketer
# Register your models here.
class CricketerAdmin(admin.ModelAdmin):
	list_display = ('name',)
admin.site.register(Cricketer, CricketerAdmin)