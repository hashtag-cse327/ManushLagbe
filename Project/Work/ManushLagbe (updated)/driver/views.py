from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Driver


# Create your views here.

class DriverView(TemplateView):
	template_name = 'driver.html'

class SdriverView(TemplateView):
	template_name = 'sdriver.html'

def driver_form_submission(request):
	print("Your data is saved!!!")
	name = request.POST['name']
	mob = request.POST['mob']
	address = request.POST['address']
	gender = request.POST['gender']
	age = request.POST['age']
	transmission = request.POST['transmission']
	auto_price = request.POST['auto_price']
	manual_price = request.POST['manual_price']


	driver = Driver(name=name,mob=mob,
		address=address,gender=gender,age=age, transmission = transmission, auto_price = auto_price, manual_price =manual_price)

	driver.save()

	return render(request, 'sindex.html')

	
