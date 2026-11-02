from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse

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
    return render(request,"login.html")