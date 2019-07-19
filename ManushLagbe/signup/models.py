from django.db import models

class Registeration(models.Model):
	name = models.CharField(max_length = 200)
	email = models.CharField(max_length = 200)
	phone = models.CharField(max_length = 11)
	password = models.CharField(max_length = 100)
