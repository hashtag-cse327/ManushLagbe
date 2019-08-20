from django.urls import path
from . import views
from django.shortcuts import render
from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from .forms import LoginForm, LoginUsernameForm  #import classes from forms.py 


def login_page(request):
	username = LoginUsernameForm(request.POST or None)
	form = LoginForm(request.POST or None)
	context = {
		"username": username,
		"form": form,
	}
	print("User logged in")
	#print(request.user.is_authenticated())
	if form.is_valid():
		print(form.cleaned_data)		#cleaned_data check validation data and print show the data in teminal

	if username.is_valid():
		print(username.cleaned_data)	#cleaned_data check validation data and print show the data in teminal

		Username = username.cleaned_data.get("username")
		Password = form.cleaned_data.get("password")
		user = authenticate(request, username=Username, password=Password)
		print(user)
		#print(request.user.is_authenticated())
		if user is not None:
			#print(request.user.is_authenticated())
			login(request, user)
			#Redirect to a success page.
			#context['form'] = LoginForm()
			return redirect("/")
		else:
			#Return an 'invalid login' error message.
			print ("Errror")
			
	return render(request, "login.html", context)
