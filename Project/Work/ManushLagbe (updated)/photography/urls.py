from django.urls import path, include
from . import views

urlpatterns = [    
    path('photography-service/', views.PhotoView.as_view(), name='photo'),   
]