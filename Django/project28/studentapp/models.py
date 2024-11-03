from django.db import models

# Create your models here.
class StudentTable(models.Model):
	name = models.CharField(max_length=50)
	roll_no = models.IntegerField()
	subject = models.CharField(max_length=50)
	marks = models.IntegerField()
