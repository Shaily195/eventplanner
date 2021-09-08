from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout
from event_manager.models import category,sponsers,Event


def home(request):
    eve=Event.objects.all()
    return render(request, "home.html",{'eve':eve})

def signup(request):
    if request.method == "POST":
        fn = request.POST['fname']
        ln = request.POST['lname']
        un = request.POST['uname']
        pwd = request.POST['pwd']
        em = request.POST['email']
        mob = request.POST['mob']
        addr = request.POST['address']
        type = request.POST['type']
        

        uobj = User(first_name=fn, last_name=ln, username=un, password=make_password(pwd), email=em)
        uobj.save()

        user_pro_obj = UserProfile(user=uobj, usertype=type,mobile=mob, address=addr)
        user_pro_obj.save()

        return redirect('/signup/')

    return render(request, "registration.html")

def login_call(request):
    if request.method == "POST":
        un = request.POST['uname']
        pwd = request.POST['pwd']

        user = authenticate(username=un, password=pwd)
        if user:
            login(request, user)
            #user---->role (seller/buyer)
            #request.user
            profileObj = UserProfile.objects.get(user__username=request.user)
            if profileObj.usertype == 'event_manager':
                return redirect('/event_manager/home/')

            elif profileObj.usertype == "event_user":
                return redirect('/event_user/user_event/')
        else:
            return HttpResponse("<h1>Invalid Credentials</h1>")


    return render(request, "registration.html")

def logout_call(request):
    logout(request)
    return redirect('/login/')  