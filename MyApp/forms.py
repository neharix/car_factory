from django import forms
from django.forms import ModelForm

from .models import Car, User

choices = [
    [f"{obj.pk}", f"{obj.first_name} {obj.last_name}"] for obj in User.objects.all()
]


class CarForm(ModelForm):
    users = forms.MultipleChoiceField(
        choices=choices, widget=forms.SelectMultiple(attrs={"class": "form-control"})
    )

    class Meta:
        model = Car
        fields = (
            "car_name",
            "car_desc",
            "image",
            "users",
            "vehicle_type",
            "color",
            "car_year",
            "vehicle_number",
        )
        widgets = {
            "car_name": forms.TextInput(attrs={"class": "form-control"}),
            "car_desc": forms.Textarea(attrs={"class": "form-control", "rows": "5"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "color": forms.Select(attrs={"class": "form-control"}),
            "vehicle_type": forms.Select(attrs={"class": "form-control"}),
            "car_year": forms.Select(attrs={"class": "form-control"}),
            "vehicle_number": forms.TextInput(attrs={"class": "form-control"}),
        }


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "father_name",
            "username",
            "phone_number",
            "password",
            "email",
            "documents",
            "passport_serie",
        )
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "father_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "documents": forms.FileInput(attrs={"class": "form-control"}),
            "password": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "passport_serie": forms.TextInput(attrs={"class": "form-control"}),
        }
