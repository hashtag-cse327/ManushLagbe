from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Mehedi

# Create your views here.

class MehediView(TemplateView):
	template_name = 'mehedi.html'

class SmehediView(TemplateView):
	template_name = 'smehedi.html'

def mehedi_form_submission(request):
	print("Your data is saved!!!")
	name = request.POST['name']
	mob = request.POST['mob']
	address = request.POST['address']
	gender = request.POST['gender']
	age = request.POST['age']
	price_ohos = request.POST['price_ohos']
	price_ohbs = request.POST['price_ohbs']
	price_thos = request.POST['price_thos']
	price_thbs = request.POST['price_thbs']


	mehedi = Mehedi(name=name, mob=mob, address=address, gender=gender, age=age, price_ohos=price_ohos, 
		price_ohbs=price_ohbs, price_thos=price_thos, price_thbs=price_thbs)

	mehedi.save()

	return render(request, 'sindex.html')
