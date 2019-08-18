from django.urls import path, include
from . import views

urlpatterns = [    
    path('mehndi-service/', views.MehediView.as_view(), name='mehedi'),
    path('mehndi-serviceprovider/', views.SmehediView.as_view(), name='smehedi'),   
]
