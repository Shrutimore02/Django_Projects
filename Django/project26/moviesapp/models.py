from django.db import models


# Create your models here.
class MovieTable(models.Model):
	movie_name = models.CharField(max_length=50)
	hero = models.CharField(max_length=50)
	heroine = models.CharField(max_length=50)
    
