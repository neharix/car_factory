from django.contrib import admin
from .models import Car, Order, Contact, User, Color, Year, VehicleType

admin.site.register(Car)
admin.site.register(Order)
admin.site.register(Contact)
admin.site.register(User)
admin.site.register(Year)
admin.site.register(Color)
admin.site.register(VehicleType)