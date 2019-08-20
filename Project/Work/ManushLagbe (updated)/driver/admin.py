from django.contrib import admin
from .models import Driver
from .models import Driver_Customer

# Register your models here.
admin.site.register(Driver)
admin.site.register(Driver_Customer)
