from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.RegisterPage.as_view(), name = 'register'),
] 