from django.contrib import admin
from django.urls import path
from MyApp import views

urlpatterns = [
    path("home/",views.index, name = 'home'),
    path("panel/", views.panel, name= "panel"),
    path("signin/", views.signin, name="signin"),
    path("signout/",views.signout,name = "signout"),
    path("bill/",views.order,name = "bill"),
    path("panel/add_vehicle/", views.add_vehicle, name='add_vehicle'),
    path("panel/add_user/", views.add_user, name='add_user'),
    path("panel/about_vehicles/", views.about_vehicles, name="about_vehicles"),
    path("", views.home_redirecter),
    ]