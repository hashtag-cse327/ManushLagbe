from django.urls import path, include
from . import views

urlpatterns = [    
    path('volunteer-service/', views.VolunteerView.as_view(), name='volunteer'),   
    path('volunteer-serviceprovider/', views.SvolunteerView.as_view(), name='svolunteer'),   
    path('volunteer_form_submission/', views.volunteer_form_submission, name='volunteer_form_submission'),   
]
