from django.urls import path
from . import views
from django.views.generic import TemplateView


# Create your views here.

class RegisterPage(TemplateView):
	template_name = 'register.html'

