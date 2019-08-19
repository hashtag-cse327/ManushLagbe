from django.urls import path
from . import views
from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Volunteer
from .models import Customer_volunteer


# Create your views here.

class VolunteerView(TemplateView):
	template_name = 'volunteer.html' #loading template volunteer.html file


class SvolunteerView(TemplateView):
	template_name = 'svolunteer.html' #loading the html file of service provider's volunteer file

# class Volunteer_list(ListView):
# 	template_name = 'v_list.html'

# 	def get_queryset(self):
# 		return Volunteer.objects.all()

def volunteer_form_submission(request):
	print("Your data is saved!!!")
	name = request.POST['name']
	mob = request.POST['mob']               #data from form is saved in the variables
	address = request.POST['address']
	gender = request.POST['gender']
	age = request.POST['age']
	price = request.POST['price']

	volunteer = Volunteer(name=name,mob=mob,
		address=address,gender=gender,age=age,price=price)  #data is copied to the database's table from the variables

	volunteer.save()

	return render(request, 'sindex.html')  #data saved

def volunteer_search(request):
	print("Your data is saved!!!")
	name = request.POST['name']
	mob = request.POST['mob']                      #saving data in variables from customers of volunteer
	address = request.POST['address']
	event = request.POST['event']
	number = request.POST['number']
	hours = request.POST['hours']

	customer_volunteer = Customer_volunteer(name=name,mob=mob,
		address=address,event_type=event,volunteer_number=number,hours=hours)  #moving data to db

	customer_volunteer.save()     #saving data in db
	volunteers= Volunteer.objects.all()
	context={
		"object_list": volunteers,                           #fetching data from database
	}
	return render(request,"v_list.html",context)

	return render(request, 'v_list.html')

# def volunteer_list(request):
# 	volunteers= Volunteer.objects.all()
# 	context={
# 		"object_list": volunteers,                           #fetching data from database
# 	}
# 	return render(request,"v_list.html",context)


