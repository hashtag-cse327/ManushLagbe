from django.urls import path, include
from . import views

urlpatterns = [    
    path('volunteer-service/', views.VolunteerView.as_view(), name='volunteer'),   
    path('volunteer-serviceprovider/', views.SvolunteerView.as_view(), name='svolunteer'),   
]
