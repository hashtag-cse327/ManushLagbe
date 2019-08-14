from django.urls import path
from . import views
from django.views.generic import TemplateView

# Create your views here.

class MehediView(TemplateView):
	template_name = 'mehedi.html'