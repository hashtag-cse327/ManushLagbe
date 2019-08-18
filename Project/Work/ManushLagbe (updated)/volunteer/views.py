from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Volunteer

# Create your views here.

class VolunteerView(TemplateView):
	template_name = 'volunteer.html'

class SvolunteerView(TemplateView):
	template_name = 'svolunteer.html'

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
