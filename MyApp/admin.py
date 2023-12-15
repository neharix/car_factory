from django.contrib import admin

from .models import Car, Color, User, VehicleType, Year

admin.site.register(Car)
admin.site.register(User)
admin.site.register(Year)
admin.site.register(Color)
admin.site.register(VehicleType)
