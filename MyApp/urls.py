from django.contrib import admin
from django.urls import path
from MyApp import views

urlpatterns = [
    path("home/", views.panel, name="panel"),
    path("signin/", views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
    path("add_vehicle/", views.add_vehicle, name="add_vehicle"),
    path("add_user/", views.add_user, name="add_user"),
    path("add_sample/", views.add_sample, name="add_sample"),
    path("about_vehicles/", views.about_vehicles, name="about_vehicles"),
    path("about_users/", views.about_users, name="about_users"),
    path("about_vehicle/<int:car_id>", views.about_vehicle),
    path("about_users/pdf/<int:user_id>/", views.view_user_pdf, name="view_user_pdf"),
    path("samples/", views.sample_table, name="samples"),
    path("samples/pdf/<int:sample_id>/", views.view_sample_pdf),
    path("about_vehicles/pdf/<int:car_id>/", views.view_car_pdf, name="view_car_pdf"),
    path("", views.home_redirecter),
]
