from django.urls import path, include
from . import views


#pathways to the required pages
urlpatterns = [    
    path('mehndi-service/', views.MehediView.as_view(), name='mehedi'),
    path('mehndi-serviceprovider/', views.SmehediView.as_view(), name='smehedi'),  
    path('mehedi_form_submission/', views.mehedi_form_submission, name='mehedi_form_submission'),
    path('mehedi_customer_form_submission/', views.mehedi_customer_form_submission, name='mehedi_customer_form_submission'),
    path('mehedi_artist_list/', views.mehedi_customer_form_submission, name='mehedi_artist_list'),
]
