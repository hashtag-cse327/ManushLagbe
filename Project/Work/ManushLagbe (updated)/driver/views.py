from django.urls import path
from . import views
from django.views.generic import TemplateView

# Create your views here.

class DriverView(TemplateView):
	template_name = 'driver.html'

class SdriverView(TemplateView):
	template_name = 'sdriver.html'
