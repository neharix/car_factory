from django.contrib import admin
from django.urls import path

from MyApp import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path(
        "search_car/",
        views.SearchCarResultsListView.as_view(),
        name="search_car_results",
    ),
    path(
        "search_user/",
        views.SearchUserResultsListView.as_view(),
        name="search_user_results",
    ),
    path(
        "search_sample/",
        views.SearchSampleResultsListView.as_view(),
        name="search_sample_results",
    ),
    path("home/panel", views.panel, name="panel"),
    path("signin/", views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
    path("mailbox/", views.mailbox, name="mailbox"),
    path("mailbox/mail/<int:letter_id>", views.read_letter, name="read_letter"),
    path("send_letter/", views.send_letter, name="send_letter"),
    path("add_vehicle/", views.add_vehicle, name="add_vehicle"),
    path("add_user/", views.add_user, name="add_user"),
    path("about_users/delete/<int:pk>", views.delete_user),
    path("about_vehicles/delete/<int:pk>", views.delete_vehicle),
    path("samples/delete/<int:pk>", views.delete_sample),
    path("add_sample/", views.add_sample, name="add_sample"),
    path("about_vehicles/", views.about_vehicles, name="about_vehicles"),
    path("about_users/", views.about_users, name="about_users"),
    path("about_vehicle/<int:car_id>", views.about_vehicle),
    path("about_user/<int:user_id>", views.about_user),
    path("about_users/pdf/<int:user_id>/", views.view_user_pdf, name="view_user_pdf"),
    path("samples/", views.sample_table, name="samples"),
    path("samples/pdf/<int:sample_id>/", views.view_sample_pdf),
    path("about_vehicles/pdf/<int:car_id>/", views.view_car_pdf, name="view_car_pdf"),
    path("", views.home_redirecter),
]
