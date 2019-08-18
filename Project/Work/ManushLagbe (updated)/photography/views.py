from django.urls import path
from . import views
from django.views.generic import TemplateView

# Create your views here.

class PhotoView(TemplateView):
	template_name = 'photography.html'

class SphotoView(TemplateView):
	template_name = 'sphotography.html'
