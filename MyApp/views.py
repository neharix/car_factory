import os
import shutil

import docx2pdf
import pythoncom
import win32com.client
import win32com.client.makepy
import winerror
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from win32com.client.dynamic import ERRORS_BAD_CONTEXT

from .forms import CarForm, UserForm
from .models import Car, Order


def pdf_to_word(input_file, output_file):
    ERRORS_BAD_CONTEXT.append(winerror.E_NOTIMPL)
    src = os.path.abspath(input_file)

    pythoncom.CoInitializeEx(0)
    win32com.client.makepy.GenerateFromTypeLibSpec("Acrobat")
    adobe = win32com.client.DispatchEx("AcroExch.App")
    avDoc = win32com.client.DispatchEx("AcroExch.AVDoc")

    avDoc.Open(src, src)
    pdDoc = avDoc.GetPDDoc()
    jObject = pdDoc.GetJSObject()

    jObject.SaveAs(output_file, "com.adobe.acrobat.docx")
    avDoc.Close(-1)


class CarObject:
    def __init__(self, pk, name, users, vehicle_type, color, year, number, documents):
        self.pk = pk
        self.name = name
        self.users = users
        self.type = vehicle_type
        self.color = color
        self.year = year
        self.number = number
        self.documents = documents

class UserObject:
    def __init__(self, pk, first_name, last_name, father_name, username, email, phone_number, passport_serie, vehicles, document, pdf_document):
        self.pk = pk
        self.first_name = first_name
        self.last_name = last_name
        self.father_name = father_name
        self.username = username
        self.email = email
        self.phone_number = phone_number
        self.passport_serie = passport_serie
        self.vehicles = vehicles
        self.documents = document
        self.pdf_document = pdf_document

def index(request):
    return render(request,"index.html")

def home_redirecter(request):
    return redirect("home")

def signin(request):
    if request.method == "POST":
        loginusername = request.POST["loginusername"]
        loginpassword = request.POST["loginpassword"]

        user = authenticate(username = loginusername,password = loginpassword)
        if user is not None:
            login(request, user)
            # messages.success(request,"Successfully logged in!")
            return redirect("panel")
        else:
            messages.error(request,"Ýalňyş maglumat girizildi!")
            return redirect("signin")

    else:
        print("error")
        return render(request,"login.html")

@login_required(login_url="signin")
def signout(request):
        logout(request)
        # messages.success(request,"Successfully logged out!")
        return redirect("home")
    
    # return HttpResponse("signout")

@login_required(login_url="signin")
def panel(request):
    if request.user.is_staff or request.user.is_superuser:
        cars = Car.objects.all()
        params = {"cars": cars}
        return render(request,"for_staff.html ", params)
    else:
        return render(request, "for_default.html")

@login_required(login_url="signin")
def add_vehicle(request):
    if request.user.is_staff or request.user.is_superuser:
        if request.method == "POST":
            form = CarForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Ulag hasaba alyndy!")
            return redirect("panel")
        else:
            context = {"form": CarForm()}
            return render(request, "add_vehicle.html", context)
    else:
        return redirect("home")

@login_required(login_url="signin")
def add_user(request):
    if request.user.is_staff or request.user.is_superuser:
        if request.method == "POST":
            form = UserForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Ulanyjy hasaba alyndy!")
                user = get_user_model().objects.last()
                file_name = str(user.documents).split("/")[len(str(user.documents).split("/")) - 1]
                file_format = str(user.documents).split(".")[len(str(user.documents).split(".")) - 1]
                base_dir = str(settings.BASE_DIR).replace("\\", "/")
                if file_format == "pdf":
                    pdf_to_word(base_dir + f"/media/user/documents/{file_name}", base_dir + f"/media/user/documents/{file_name.split(".")[0]}.docx")
                    shutil.copy2(base_dir + f"/media/user/documents/{file_name}", base_dir + f"/media/user/pdf_documents/{file_name}")
                    os.remove(base_dir + f"/media/user/documents/{file_name}")
                    user.documents = f"user/documents/{file_name.split(".")[0]}.docx"
                    user.pdf_documents = f"user/pdf_documents/{file_name}"
                    user.save()
                elif file_format == "docx":
                    pythoncom.CoInitializeEx(0)
                    pdf = docx2pdf.convert(base_dir + f"/media/user/documents/{file_name}", base_dir + f"/media/user/pdf_documents/{file_name.split(".")[0]}.pdf")
                    user.pdf_documents = f"user/pdf_documents/{file_name.split(".")[0]}.pdf"
                    user.save()
            return redirect("panel")
        else:
            context = {"form": UserForm()}
            return render(request, "add_user.html", context)
    else:
        return redirect("home")

@login_required(login_url="signin")
def about_vehicles(request):
    if request.user.is_staff or request.user.is_superuser:
        cars = Car.objects.all().order_by("pk")
        car_obj = []
        for car in cars:
            user_list = []
            users = Car.objects.get(pk=car.pk).users.all()
            for user in users:
                user_list.append(f"{user.first_name} {user.last_name}")
            car_obj.append(CarObject(car.pk, car.car_name, ", ".join(user_list), car.vehicle_type.vehicle_type, car.color.color, car.car_year.year, car.vehicle_number, "something"))
        context = {"cars": car_obj}
        return render(request, "vehicle_table.html", context)
    else:
        return redirect("home")

@login_required(login_url="signin")
def about_users(request):
    if request.user.is_staff or request.user.is_superuser:
        users = get_user_model().objects.all().order_by("pk")
        user_obj = []
        for user in users:
            car = "Adyna ulag bellenilmedik"
            for car in Car.objects.all():
                for car_user in car.users.all():
                    if car_user.username == user.username:
                        car = car.car_name
            if user.is_superuser:
                continue
            else:
                user_obj.append(UserObject(user.pk, user.first_name, user.last_name, user.father_name, user.username, user.email, user.phone_number, user.passport_serie, car, user.documents, user.pdf_documents))
        context = {"users": user_obj}
        return render(request, "user_table.html", context)
    else:
        return redirect("home")

def view_pdf(request, user_id):
    user = get_user_model().objects.get(pk=user_id)
    context = {"user": user}
    return render(request, "view_pdf.html", context)

@login_required(login_url="signin")
def bill(request):
    cars = Car.objects.all()
    params = {"cars":cars}
    return render(request,"bill.html",params)

@login_required(login_url="signin")
def order(request):
    if request.method == "POST":
        billname = request.POST.get("billname","")
        billemail = request.POST.get("billemail","")
        billphone = request.POST.get("billphone","")
        billaddress = request.POST.get("billaddress","")
        billcity = request.POST.get("billcity","")
        cars11 = request.POST["cars11"]
        dayss = request.POST.get("dayss","")
        date = request.POST.get("date","")
        fl = request.POST.get("fl","")
        tl = request.POST.get("tl","")
        # print(request.POST["cars11"])
        
        order = Order(name = billname,email = billemail,phone = billphone,address = billaddress,city=billcity,cars = cars11,days_for_rent = dayss,date = date,loc_from = fl,loc_to = tl)
        order.save()
        return redirect("home")
    else:
        print("error")
        return render(request,"bill.html")
