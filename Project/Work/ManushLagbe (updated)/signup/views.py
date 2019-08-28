from django.contrib.auth import authenticate, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views.generic import TemplateView


# Create your views here.
User = get_user_model()
def register_page(request):                     #defines function  register_page
    form = RegisterForm(request.POST or None)
    context = {
        "form": form,
    }
    if 'customer' in request.POST:
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            new_user = User.objects.create_user(username, email, password)
            new_user.is_staff= False                                           #is_staff set to false to identify the customers
            new_user.save()
            print(new_user)
            return redirect("login")
    elif 'serviceProvider' in request.POST:
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            new_user = User.objects.create_user(username, email, password)
            new_user.is_staff= True                                             #is_staff set to true to identify the service providers
            new_user.save()
            print(new_user)
            return redirect("login")
    return render(request, "register.html", context)
