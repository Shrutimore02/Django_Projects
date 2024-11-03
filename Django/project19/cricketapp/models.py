from django.db import models

# Create your models here.
class CricketData(models.Model):
	name = models.CharField(max_length=15)
	age = models.IntegerField()
	role = models.CharField(max_length=10)
	city = models.CharField(max_length=15)
	dob = models.DateField()

	class Meta:
		verbose_name = "CricketData"
		verbose_name_plural = "CricketData"

		def __str__(self):
			return self.name
	    
