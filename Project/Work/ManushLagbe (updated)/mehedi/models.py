from django.db import models

# Create your models here.

class Mehedi(models.Model):
	name = models.CharField(max_length=200)
	mob = models.CharField(max_length=20)
	address = models.CharField(max_length=500)
	gender = models.CharField(max_length=20)
	age = models.CharField(max_length=20)
	price_ohos = models.IntegerField()
	price_ohbs = models.IntegerField()
	price_thos = models.IntegerField()
	price_thbs = models.IntegerField()

	def __str__(self):
		return self.name

class Mehedi_Customer(models.Model):
	name = models.CharField(max_length=200)
	mob = models.CharField(max_length=20)
	address = models.CharField(max_length=500)

	hand = models.CharField(max_length=50)
	no_of_artist = models.IntegerField()

	def __str__(self):
		return self.name
