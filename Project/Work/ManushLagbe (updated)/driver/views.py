from django.urls import path
from . import views
from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Driver
from .models import Driver_Customer


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

def driver_customer_form_submission(request):
	print("Your data is saved!!!")
	name = request.POST['name']
	mob = request.POST['mob']
	address = request.POST['address']					#defining the tables and making a view to show as a list
	transmission = request.POST['transmission']
	hours = request.POST['hours']

	driver_customer = Driver_Customer(name=name, mob=mob, address=address, transmission=transmission, 
						hours=hours)

	driver_customer.save()

	drivers= Driver.objects.all()
	context={
		"object_list": drivers,                           #fetches data from database of driver and shows as a list in the html
	}
	return render(request,'dsp.html',context)

	return render(request, 'dsp.html')

	
