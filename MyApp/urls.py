from django.contrib import admin
from django.urls import path

from MyApp import views

urlpatterns = [
    path("home/", views.index, name="home"),
    path("panel/", views.panel, name="panel"),
    path("signin/", views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
    path("panel/add_vehicle/", views.add_vehicle, name="add_vehicle"),
    path("panel/add_user/", views.add_user, name="add_user"),
    path("panel/add_sample/", views.add_sample, name="add_sample"),
    path("panel/about_vehicles/", views.about_vehicles, name="about_vehicles"),
    path("panel/about_users/", views.about_users, name="about_users"),
    path("panel/about_vehicle/<int:car_id>", views.about_vehicle),
    path("panel/about_users/pdf/<int:user_id>/", views.view_user_pdf, name="view_user_pdf"),
    path("panel/samples/", views.sample_table, name="samples"),
    path("panel/samples/pdf/<int:sample_id>/", views.view_sample_pdf),
    path("panel/about_vehicles/pdf/<int:car_id>/", views.view_car_pdf, name="view_car_pdf"),
    path("", views.home_redirecter),
]
