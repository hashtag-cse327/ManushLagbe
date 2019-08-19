from django.db import models

# Create your models here.
class Photographer(models.Model):
	name = models.CharField(max_length=200)
	mob = models.CharField(max_length=20)
	address = models.CharField(max_length=500)
	gender = models.CharField(max_length=20)
	age = models.CharField(max_length=20)

	photographer_type = models.CharField(max_length=20)
	small_event_charge = models.IntegerField()
	large_event_charge = models.IntegerField()

	def __str__(self):
		return self.name

class Customer_Photographer(models.Model):
	name = models.CharField(max_length=200)
	mob  = models.CharField(max_length=20)
	address = models.CharField(max_length=200)

	event_type = models.CharField(max_length=50)
	number_of_photographer = models.IntegerField()

	def __str__(self):
		return self.name

