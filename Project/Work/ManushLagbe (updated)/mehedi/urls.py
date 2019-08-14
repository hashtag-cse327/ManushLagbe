from django.urls import path, include
from . import views

urlpatterns = [    
    path('mehedi-service/', views.MehediView.as_view(), name='mehedi'),   
]