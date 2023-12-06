from django.contrib import admin
from .models import Car, Order, Contact, User

admin.site.register(Car)
admin.site.register(Order)
admin.site.register(Contact)
admin.site.register(User)