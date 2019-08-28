from django.urls import path
from . import views
from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Driver
from .models import Driver_Customer
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

class DriverView(TemplateView):
	template_name = 'driver.html'


def SdriverView(request):
	return render(request,'sdriver.html')

# ---Fetches selected data from the database table  
# def search(request):
# 	if request.method == 'POST':
# 		transmission = request.POST['transmission']

# 		if transmission:
# 			match = Driver.objects.filter(Q(transmission__icontains=transmission) | Q(transmission__icontains='both') )

# 			if match:
# 				return render(request,'dsp.html',{'sr':match})
# 			else:
# 				messages.error(request,'no result found')
# 		else:
# 			return HttpResponseRedirect('/driver_customer_form_submission/')           

# 	return render(request,'driver.html')
#-----------------------------------------------------

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

	# ---Fetches selected data from the database table
	if request.method == 'POST':
		transmission = request.POST['transmission']

		if transmission:
			match = Driver.objects.filter(Q(transmission__icontains=transmission) | Q(transmission__icontains='both') )

			if match:
				return render(request,'dsp.html',{'sr':match})
			else:
				messages.error(request,'no result found')
		else:
			return HttpResponseRedirect('/driver_customer_form_submission/')
	#----------------------------------------------------------------------------------------------------------


	# drivers= Driver.objects.all()
	# context={
	# 	"object_list": drivers,                           #fetches data from database of driver and shows as a list in the html
	# }
	# return render(request,'dsp.html',context)

	return render(request, 'dsp.html')

	
