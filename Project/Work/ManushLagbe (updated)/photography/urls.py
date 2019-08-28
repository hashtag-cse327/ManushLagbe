from django.urls import path, include
from . import views

urlpatterns = [    
    path('photography-service/', views.PhotoView.as_view(), name='photo'),   
    path('photography-serviceprovider/', views.SphotoView.as_view(), name='sphoto'),  
    path('photographer_form_submission/', views.photographer_form_submission, name='photographer_form_submission'),
    #path('customer_photographer_form_submission/', views.search, name='photographer_search'),      #selected search
    path('customer_photographer_form_submission/', views.customer_photographer_form_submission, name='customer_photographer_form_submission'),    
    path('photographer_list/', views.customer_photographer_form_submission, name='photographer_list'),    
]
