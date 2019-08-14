from django.urls import path
from . import views
from django.views.generic import TemplateView

# Create your views here.

class VolunteerView(TemplateView):
	template_name = 'volunteer.html'