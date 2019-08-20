from django.db import models

# Create your models here.
class Driver(models.Model):
	name = models.CharField(max_length=200)
	mob = models.CharField(max_length=20)
	address = models.CharField(max_length=500)		   #creates a table for Driver information give
	gender = models.CharField(max_length=20)
	age = models.CharField(max_length=20)
	transmission = models.CharField(max_length=20)
	auto_price = models.IntegerField()
	manual_price = models.IntegerField()


	def __str__(self):
		return self.name

class Driver_Customer(models.Model):
	name = models.CharField(max_length=200)
	mob = models.CharField(max_length=20)
	address = models.CharField(max_length=500)			#creates a table for Customer information which will later
	transmission = models.CharField(max_length=20)
	hours = models.IntegerField()

	def __str__(self):
		return self.name

