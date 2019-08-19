from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Volunteer
from .models import Customer_volunteer

# Create your views here.

class VolunteerView(TemplateView):
	template_name = 'volunteer.html'

class SvolunteerView(TemplateView):
	template_name = 'svolunteer.html'

class Volunteer_list(TemplateView):
	template_name = 'v_list.html'

def volunteer_form_submission(request):
	print("Your data is saved!!!")
	name = request.POST['name']
	mob = request.POST['mob']
	address = request.POST['address']
	gender = request.POST['gender']
	age = request.POST['age']
	price = request.POST['price']

	volunteer = Volunteer(name=name,mob=mob,
		address=address,gender=gender,age=age,price=price)

	volunteer.save()

	return render(request, 'sindex.html')

def volunteer_search(request):
	print("Your data is saved!!!")
	name = request.POST['name']
	mob = request.POST['mob']
	address = request.POST['address']
	event = request.POST['event']
	number = request.POST['number']
	hours = request.POST['hours']

	customer_volunteer = Customer_volunteer(name=name,mob=mob,
		address=address,event_type=event,volunteer_number=number,hours=hours)

	customer_volunteer.save()

	return render(request, 'v_list.html')
