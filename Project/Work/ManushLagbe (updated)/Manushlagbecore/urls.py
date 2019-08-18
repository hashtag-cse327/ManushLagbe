from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name = 'home'),
    path('aboutus/', views.AboutPage.as_view(), name = 'aboutus'),
    path('service-provider-home/', views.ShomePage.as_view(), name = 'provider'),
] 
