from django.urls import path, include
from . import views

urlpatterns = [    
    path('mehndi-service/', views.MehediView.as_view(), name='mehedi'),
    path('mehndi-serviceprovider/', views.SmehediView.as_view(), name='smehedi'),  
    path('mehedi_form_submission/', views.mehedi_form_submission, name='mehedi_form_submission'), 
]
