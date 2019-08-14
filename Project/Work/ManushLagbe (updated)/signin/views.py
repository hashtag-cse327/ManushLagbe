from django.urls import path
from . import views
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

def login(request):
  return render(request, 'login.html')

@login_required
def home(request):
  return render(request, 'home.html') 
