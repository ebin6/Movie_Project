from django.urls import path
from actors import views

urlpatterns=[
    path("add-actor/",views.AddActor.as_view(),name="add_actor"),
    path("all-actors/",views.AllActors.as_view(),name="list_actors"),
    path("update-actor/<int:pk>",views.UpdateActor.as_view(),name="update_actor"),
    path("actor-detail/<int:pk>",views.ActorDetail.as_view(),name="actor_detail")
]