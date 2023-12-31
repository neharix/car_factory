from django.contrib.auth.models import AbstractUser
from django.db import models


class Car(models.Model):
    car_name = models.CharField(
        verbose_name="Ulagyň ady", max_length=30, default="", unique=True
    )
    car_desc = models.TextField(verbose_name="Ulag barada", default="")
    image = models.ImageField(
        verbose_name="Suraty", upload_to="car/images/", default=""
    )
    users = models.ManyToManyField("User", verbose_name="Ulanyjylar")
    color = models.ForeignKey("Color", verbose_name="Reňki", on_delete=models.PROTECT)
    car_year = models.ForeignKey("Year", verbose_name="Ýyly", on_delete=models.PROTECT)
    vehicle_number = models.CharField(max_length=10, verbose_name="Nomeri")
    vehicle_type = models.ForeignKey(
        "VehicleType", verbose_name="Görnüşi", on_delete=models.PROTECT
    )
    characteristics_docx = models.FileField(
        null=True, verbose_name="docx dokumenti", blank=True
    )
    characteristics_pdf = models.FileField(
        null=True, verbose_name="pdf dokumenti", blank=True
    )

    class Meta:
        verbose_name = "Ulag"
        verbose_name_plural = "Ulaglar"

    def __str__(self):
        return self.car_name


class Color(models.Model):
    color = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Reňk"
        verbose_name_plural = "Reňkler"

    def __str__(self):
        return self.color


class Year(models.Model):
    year = models.CharField(max_length=4)

    class Meta:
        verbose_name = "Ýyl"
        verbose_name_plural = "Ýyllar"

    def __str__(self):
        return self.year


class VehicleType(models.Model):
    vehicle_type = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Ulag görnüşi"
        verbose_name_plural = "Ulag görnüşleri"

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

    class Meta:
        verbose_name = "Ulanyjy"
        verbose_name_plural = "Ulanyjylar"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Letter(models.Model):
    user = models.CharField(max_length=200)
    text = models.TextField()
    sent = models.DateTimeField(auto_now_add=True)
    is_checked = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Hat"
        verbose_name_plural = "Hatlar"

    def __str__(self):
        return f"{self.user} {self.sent}"


class Sample(models.Model):
    name = models.CharField(max_length=250)
    documents = models.FileField(upload_to="samples/documents", blank=True, null=True)

    def __str__(self):
        return self.permission_name
