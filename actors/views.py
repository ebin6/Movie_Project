from django.shortcuts import render,redirect
from actors.forms import ActorForm
from django.http import HttpResponse
from django.views.generic import ListView,CreateView,UpdateView,DetailView
from actors.models import Actors
from django.urls import reverse_lazy

# Create your views here.


class AddActor(CreateView):
    model=Actors
    form_class=ActorForm
    template_name="add-actors.html"
    success_url=reverse_lazy("list_actors")


class AllActors(ListView):
    model=Actors
    template_name="list-actors.html"
    context_object_name="actors"

class UpdateActor(UpdateView):
    model=Actors
    form_class=ActorForm
    template_name="update-actors.html"
    success_url=reverse_lazy("list_actors")   

class ActorDetail(DetailView):
    model=Actors
    context_object_name="actor"
    template_name="actor-detail.html"