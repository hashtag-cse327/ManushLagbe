from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from signin import views

urlpatterns = [
    path('admin/', admin.site.urls),         
    path('', include('Manushlagbecore.urls')),
    path('', include('signup.urls')),
    path('', include('mehedi.urls')),
    path('', include('photography.urls')),
    path('', include('driver.urls')),
    path('', include('volunteer.urls')),
    path('login/', views.login_page, name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('social-auth/', include('social_django.urls', namespace="social")),
    
]
