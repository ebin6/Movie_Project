from django.urls  import path
from movie import views

urlpatterns=[
    path("add-movie/",views.addMovie,name="add_movie")
]