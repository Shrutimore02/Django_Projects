from django.contrib import admin
from dbapp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
	list_display = ('name',"age")
admin.site.register(Student, StudentAdmin)

