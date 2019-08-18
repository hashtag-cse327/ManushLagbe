from django.db import models

# Create your models here.
class Volunteer(models.Model):
	name = models.CharField(max_length=200)
	mob = models.CharField(max_length=20)
	address = models.CharField(max_length=500)
	gender = models.CharField(max_length=20)
	age = models.CharField(max_length=20)
	price = models.IntegerField()

	def __str__(self):
		return self.name
