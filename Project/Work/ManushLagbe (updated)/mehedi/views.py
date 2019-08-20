from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Mehedi 
from .models import Mehedi_Customer

# Create your views here.

class MehediView(TemplateView):
	template_name = 'mehedi.html'

class SmehediView(TemplateView):
	template_name = 'smehedi.html'

class Mehedi_artist_list(TemplateView):
	template_name = 'msp_list.html'

def mehedi_form_submission(request):
	print("Your data is saved!!!")
	name = request.POST['name']
	mob = request.POST['mob']
	address = request.POST['address']
	gender = request.POST['gender']
	age = request.POST['age']					#saving data to the variables for forms
	price_ohos = request.POST['price_ohos']
	price_ohbs = request.POST['price_ohbs']
	price_thos = request.POST['price_thos']
	price_thbs = request.POST['price_thbs']


	mehedi = Mehedi(name=name, mob=mob, address=address, gender=gender, age=age, price_ohos=price_ohos, 
		price_ohbs=price_ohbs, price_thos=price_thos, price_thbs=price_thbs)

	mehedi.save()

	return render(request, 'sindex.html')

def mehedi_customer_form_submission(request):
	print("Your data is saved!!!")
	name = request.POST['name']
	mob = request.POST['mob']
	address = request.POST['address']							 #saving data in variables from customers of mehedi

	hand = request.POST['hand']
	artists = request.POST['artists']

	mehedi_customer = Mehedi_Customer(name=name, mob=mob, address=address,
						hand=hand,no_of_artist=artists)

	
	mehedi_customer.save()     #saving data in db
	
	m_artist = Mehedi.objects.all()
	context={
		"object_list": m_artist,                           #fetching data from database
	}
	return render(request,'msp.html',context)

	return render(request, 'msp.html')
