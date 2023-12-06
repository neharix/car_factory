from django.contrib import admin
from django.urls import path
from MyApp import views

urlpatterns = [
    path("home/",views.index, name = 'home'),
    path("vehicles/", views.vehicles, name= "vehicles"),
    path("signin/", views.signin, name="signin"),
    path("signout/",views.signout,name = "signout"),
    path("bill/",views.order,name = "bill"),
    path("vehicles/add_vehicle/", views.add_vehicle, name='add_vehicle'),
    path("", views.home_redirecter),
    ]