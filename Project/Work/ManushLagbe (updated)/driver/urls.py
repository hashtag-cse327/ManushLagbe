from django.urls import path, include
from . import views

urlpatterns = [    
    path('driver-service/', views.DriverView.as_view(), name='driver'),   
]