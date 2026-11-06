from django.shortcuts import render,redirect
from actors.forms import ActorForm
from django.http import HttpResponse

# Create your views here.


def addActor(request):
    if request.method=="POST":
        form=ActorForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return HttpResponse("Invalid data")
    else:
        form=ActorForm()
    return render(request,"add-actors.html",{"my_form":form})