from django.urls import path
from actors import views

urlpatterns=[
    path("add-actor/",views.addActor,name="add_actor"),
]