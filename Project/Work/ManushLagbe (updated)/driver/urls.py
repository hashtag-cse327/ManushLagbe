from django.urls import path, include
from . import views

urlpatterns = [    
    path('driver-service/', views.DriverView.as_view(), name='driver'),   
    path('driver-serviceprovider/', views.SdriverView.as_view(), name='sdriver'),  
    path('driver_form_submission/', views.driver_form_submission, name='driver_form_submission'),   
]
