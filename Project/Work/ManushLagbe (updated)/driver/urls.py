from django.urls import path, include
from . import views

#here all the pathways are mentioned which leads to the desired page
#when a request is made
urlpatterns = [    
    path('driver-service/', views.DriverView.as_view(), name='driver'),   
    path('driver-serviceprovider/', views.SdriverView, name='sdriver'),  
    path('driver_form_submission/', views.driver_form_submission, name='driver_form_submission'), 
    path('driver_customer_form_submission/', views.driver_customer_form_submission, name='driver_customer_form_submission'), #selected search + customer data saved to database
   # path('driver_customer_form_submission/', views.search, name='driver_search'),      #selected search
    path('driver_list/', views.driver_customer_form_submission, name='driver_list'),  
]
