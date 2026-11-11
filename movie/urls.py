from django.urls  import path
from movie import views

urlpatterns=[
    path("",views.home,name="index"),
    path("add-movie/",views.addMovie,name="add_movie"),
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/category/<slug:slug>/', views.category_movies, name='category_movies'),
    path("update-movie/<int:movie_id>",views.updateMovie,name="edit_movie"),
    path("details/<int:movie_id>/",views.movieDetail,name="movie_detail"),
    path("delete/<int:movie_id>/",views.deleteMovie,name="delete_movie")
]