from django.contrib.auth.models import AbstractUser
from django.db import models


class Car(models.Model):
    car_name = models.CharField(max_length=30, default="")
    car_desc = models.TextField(default="")
    image = models.ImageField(upload_to="car/images/", default="")
    users = models.ManyToManyField("User", verbose_name="Ulanyjylar")
    color = models.ForeignKey("Color", on_delete=models.PROTECT)
    car_year = models.ForeignKey("Year", on_delete=models.PROTECT)
    vehicle_number = models.CharField(max_length=10)
    vehicle_type = models.ForeignKey("VehicleType", on_delete=models.PROTECT)
    characteristics_docx = models.FileField(null=True, blank=True)
    characteristics_pdf = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.car_name


class Color(models.Model):
    color = models.CharField(max_length=30)

    def __str__(self):
        return self.color


class Year(models.Model):
    year = models.CharField(max_length=4)

    def __str__(self):
        return self.year


class VehicleType(models.Model):
    vehicle_type = models.CharField(max_length=30)

    def __str__(self):
        return self.vehicle_type


class User(AbstractUser):
    father_name = models.CharField(verbose_name="Atasynyň ady", max_length=40)
    username = models.CharField(verbose_name="Ulanyjy ady", max_length=200, unique=True)
    email = models.EmailField(verbose_name="E-Mail", null=True, blank=True)
    passport_serie = models.CharField(verbose_name="Pasport nomeri", max_length=20)
    phone_number = models.CharField(verbose_name="Telefon nomeri", max_length=12)
    documents = models.FileField(upload_to="user/documents", null=True, blank=True)
    pdf_documents = models.FileField(null=True, blank=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Sample(models.Model):
    name = models.CharField(max_length=250)
    url = models.URLField(blank=True, null=True)
    documents = models.FileField(upload_to="samples/documents", blank=True, null=True)

    def __str__(self):
        return self.permission_name