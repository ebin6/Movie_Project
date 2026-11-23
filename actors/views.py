from actors.forms import ActorForm
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from actors.models import Actors
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from accounts.decorators import superuser_required


@method_decorator(superuser_required, name="dispatch")
class AddActor(CreateView):
    model = Actors
    form_class = ActorForm
    template_name = "add-update-actors.html"
    success_url = reverse_lazy("list_actors")


class AllActors(ListView):
    model = Actors
    template_name = "list-actors.html"
    context_object_name = "actors"


@method_decorator(superuser_required, name="dispatch")
class UpdateActor(UpdateView):
    model = Actors
    form_class = ActorForm
    template_name = "add-update-actors.html"
    success_url = reverse_lazy("list_actors")


class ActorDetail(DetailView):
    model = Actors
    context_object_name = "actor"
    template_name = "actor-detail.html"


@method_decorator(superuser_required, name="dispatch")
class DeleteActor(DeleteView):
    model = Actors
    template_name = "actor-confirm-delete.html"
    context_object_name = "actor"
    success_url = reverse_lazy("list_actors")
