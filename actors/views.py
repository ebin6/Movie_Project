from django.shortcuts import render
from actors.forms import ActorForm

# Create your views here.


def addActor(request):
    form=ActorForm()
    return render(request,"add-actors.html",{"my_form":form})