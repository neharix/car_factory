# from email.mime import message
# from pyexpat import model
from django.http import Http404, HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Car, Order, Contact
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,'index.html')

def home_redirecter(request):
    return redirect('home')

def signin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username = loginusername,password = loginpassword)
        if user is not None:
            login(request, user)
            # messages.success(request,"Successfully logged in!")
            return redirect('vehicles')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('signin')

    else:
        print("error")
        return render(request,'login.html')

@login_required(login_url='signin')
def signout(request):
        logout(request)
        # messages.success(request,"Successfully logged out!")
        return redirect('home')
    
    # return HttpResponse('signout')

@login_required(login_url='signin')
def vehicles(request):
    if request.user.is_staff or request.user.is_superuser:
        cars = Car.objects.all()
        params = {'car':cars}
        return render(request,'for_staff.html ',params)
    else:
        return render(request, 'for_default.html')

@login_required(login_url='signin')
def add_vehicle(request):
    if request.user.is_staff or request.user.is_superuser:
        return render(request, 'add_vehicle.html')
    else:
        return redirect('home')

@login_required(login_url='signin')
def bill(request):
    cars = Car.objects.all()
    params = {'cars':cars}
    return render(request,'bill.html',params)

@login_required(login_url='signin')
def order(request):
    if request.method == "POST":
        billname = request.POST.get('billname','')
        billemail = request.POST.get('billemail','')
        billphone = request.POST.get('billphone','')
        billaddress = request.POST.get('billaddress','')
        billcity = request.POST.get('billcity','')
        cars11 = request.POST['cars11']
        dayss = request.POST.get('dayss','')
        date = request.POST.get('date','')
        fl = request.POST.get('fl','')
        tl = request.POST.get('tl','')
        # print(request.POST['cars11'])
        
        order = Order(name = billname,email = billemail,phone = billphone,address = billaddress,city=billcity,cars = cars11,days_for_rent = dayss,date = date,loc_from = fl,loc_to = tl)
        order.save()
        return redirect('home')
    else:
        print("error")
        return render(request,'bill.html')