from django.shortcuts import render

# Create your views here.

def signUp(request):
    return render(request,"register.html")


def signIn(request):
    return render(request,"login.html")