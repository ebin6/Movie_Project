from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def signUp(request):
    if request.method=="POST":
        email=request.POST['email']
        f_name=request.POST["first_name"]
        l_name=request.POST['last_name']
        password=request.POST['password']
        if User.objects.filter(username=email).exists():
            return HttpResponse("Username already exists")
        else:
            user=User.objects.create_user(username=email,first_name=f_name,last_name=l_name,password=password)
            user.save()
            return redirect("login")
    return render(request,"register.html")


def signIn(request):
    if request.method=="POST":
        username=request.POST['username']
        passwd=request.POST['password']
        user=auth.authenticate(username=username,password=passwd)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            return HttpResponse("Invalid username or password")
        
    return render(request,"login.html")

@login_required(login_url="login")
def Logout(request):
    auth.logout(request)
    return redirect("/")