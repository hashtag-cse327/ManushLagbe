from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Photographer
from .models import Customer_Photographer
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

class PhotoView(TemplateView):
	template_name = 'photography.html' #loading template photography.html file

class SphotoView(TemplateView):
	template_name = 'sphotography.html' #loading the html file of service provider's photographer file

#class Photographer_list(TemplateView):
#	template_name = 'p_list.html'

# ---Fetches selected data from the database table  
# def search(request):
# 	if request.method == 'POST':
# 		etype = request.POST['etype']

# 		if etype:
# 			match = Photographer.objects.filter(Q(photographer_type__icontains=etype) | Q(photographer_type__icontains='both') )

# 			if match:
# 				return render(request,'p_list.html',{'sr':match})
# 			else:
# 				messages.error(request,'No Result Found')
# 		else:
# 			return HttpResponseRedirect('/customer_photographer_form_submission/')           

# 	return render(request,'photography.html')
#-----------------------------------------------------

def photographer_form_submission(request):
	print("Your data is saved!!!")
	name = request.POST['name']
	mob = request.POST['mob']
	address = request.POST['address']		#data from form is saved in the variables
	gender = request.POST['gender']			
	age = request.POST['age']

	ptype = request.POST['ptype']
	se_charge = request.POST['se_charge']
	le_charge = request.POST['le_charge']


	photographer = Photographer(name=name,mob=mob,
		address=address,gender=gender,age=age,photographer_type=ptype,
		small_event_charge=se_charge,large_event_charge=le_charge)

	photographer.save() #data saved

	return render(request, 'sindex.html')

def customer_photographer_form_submission(request):
	print("Your data is saved!!!")
	name = request.POST['name']
	mob = request.POST['mob']
	address = request.POST['address']

	etype = request.POST['etype']
	photographer_number = request.POST['photographer_number']

	customer_photographer = Customer_Photographer(name=name,mob=mob,address=address,
			event_type=etype, number_of_photographer = photographer_number)

	customer_photographer.save()

	# photographers = Photographer.objects.all()
	# context={
	# 	"object_list": photographers,
	# }
	# return render(request, "p_list.html", context)

	# ---Fetches selected data from the database table  
	if request.method == 'POST':
		etype = request.POST['etype']

		if etype:
			match = Photographer.objects.filter(Q(photographer_type__icontains=etype) | Q(photographer_type__icontains='both') )

			if match:
				return render(request,'p_list.html',{'sr':match})
			else:
				messages.error(request,'No Result Found')
		else:
			return HttpResponseRedirect('/customer_photographer_form_submission/')
		#-----------------------------------------------------



	return render(request, 'p_list.html')


