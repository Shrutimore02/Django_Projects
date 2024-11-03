from django.db import models

# Create your models here.
class EmployeeData(models.Model):
	name = models.CharField(max_length=50)
	job = models.CharField(max_length=30)
	salary = models.IntegerField()
	class Meta:
		verbose_name = "EmployeeData"
		verbose_name_plural = "EmployeeDatas"

	def __str__(self):
		return self.name
