from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Car, Color, Letter, User, VehicleType, Year

admin.site.register(Car)
admin.site.register(User)
admin.site.register(Year)
admin.site.register(Color)
admin.site.register(VehicleType)
admin.site.register(Letter)

admin.site.unregister(Group)
