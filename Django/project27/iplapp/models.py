from django.db import models

# Create your models here.
class CSKTable(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	country = models.CharField(max_length=50)
	marital_status = models.CharField(max_length=50)
	role = models.CharField(max_length=50)

  
class DCTable(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	country = models.CharField(max_length=50)
	marital_status = models.CharField(max_length=50)
	role = models.CharField(max_length=50)

class GTTable(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	country = models.CharField(max_length=50)
	marital_status = models.CharField(max_length=50)
	role = models.CharField(max_length=50)

class KKRTable(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	country = models.CharField(max_length=50)
	marital_status = models.CharField(max_length=50)
	role = models.CharField(max_length=50)


class LSGTable(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	country = models.CharField(max_length=50)
	marital_status = models.CharField(max_length=50)
	role = models.CharField(max_length=50)

class MITable(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	country = models.CharField(max_length=50)
	marital_status = models.CharField(max_length=50)
	role = models.CharField(max_length=50)


class PKTable(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	country = models.CharField(max_length=50)
	marital_status = models.CharField(max_length=50)
	role = models.CharField(max_length=50)


class RCBTable(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	country = models.CharField(max_length=50)
	marital_status = models.CharField(max_length=50)
	role = models.CharField(max_length=50)


class RRTable(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	country = models.CharField(max_length=50)
	marital_status = models.CharField(max_length=50)
	role = models.CharField(max_length=50)


class SRHTable(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	country = models.CharField(max_length=50)
	marital_status = models.CharField(max_length=50)
	role = models.CharField(max_length=50)





