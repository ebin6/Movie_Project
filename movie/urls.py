from django.urls  import path
from movie import views

urlpatterns=[
    path("add-movie/",views.addMovie,name="add_movie"),
    path('movies/', views.movie_list, name='movie_list'),
    path("update-movie/<int:movie_id>",views.updateMovie,name="edit_movie"),
]