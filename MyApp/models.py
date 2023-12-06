from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

class Car(models.Model):
    car_id = models.IntegerField(default=0)
    car_name = models.CharField(max_length=30,default="")
    car_desc = models.CharField(max_length=300,default="")
    image = models.ImageField(upload_to="car/images",default="")
    users = models.ManyToManyField("User" ,verbose_name="Ulanyjylar")
    color = models.ForeignKey("Color", on_delete=models.PROTECT)
    car_year = models.ForeignKey("Year", on_delete=models.PROTECT)
    vehicle_number = models.CharField(max_length=10)

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
    
class User(AbstractUser):
    father_name = models.CharField(verbose_name="Atasynyň ady", max_length=40)
    username = models.CharField(verbose_name="Ulanyjy ady", max_length=200, unique=True)
    email = models.EmailField(verbose_name="E-Mail" ,null=True)
    passport_serie = models.CharField(verbose_name="Pasport nomeri" ,max_length=20)
    phone_number = models.CharField(verbose_name="Telefon nomeri", max_length=10)
    documents = models.FileField(upload_to="user/documents", null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    

class Order(models.Model) :
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=90,default="")
    email = models.CharField(max_length=50,default="")
    phone = models.CharField(max_length=20,default="")
    address = models.CharField(max_length=500,default="")
    city = models.CharField(max_length=50,default="")
    cars = models.CharField(max_length=50,default="")
    days_for_rent = models.IntegerField(default=0)
    date = models.CharField(max_length=50,default="")
    loc_from = models.CharField(max_length=50,default="")
    loc_to = models.CharField(max_length=50,default="")
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    message = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150,default="")
    email = models.CharField(max_length=150,default="")
    phone_number = models.CharField(max_length=15,default="")
    message = models.TextField(max_length=500,default="")

    def __str__(self) :
        return self.name
