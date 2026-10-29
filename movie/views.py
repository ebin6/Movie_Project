from django.shortcuts import render,redirect
from movie.models import Category,Movie
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"index.html")

def addMovie(request):
    if request.method=="POST":
        movie=request.POST["movie"]
        tr_link=request.POST['trailer_link']
        cate=request.POST['category']
        re_date=request.POST['release_date']
        poster=request.FILES["poster"]
        desc=request.POST["description"]
        rating=request.POST["rating"]
        category=Category.objects.get(id=cate)
        Movie(movie=movie,trailer_link=tr_link,
              category=category,release_date=re_date,
              poster=poster,description=desc,rating=rating).save()
        return redirect("movie_list")

    categories=Category.objects.all()
    return render(request,"add-movie.html",{"categories":categories})


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'all-movies.html', {'movies': movies})

"""
First we are sending GET request and the update page is displayed . So the categories are fetched to view categories in dropdown .
Movie details is fecthed with id (movie_id) So that the exiting image and value are provided in input fields .
After submittng the form we are getting POST request , every values are fetched with 
name attribute value and assigned in corresponding variable .
We had stored the object which is need to be updated in movie ( movie=Movie.objects.get(id=movie_id) ).
Assign the new values to its attributes ( column names ) .
Eg :
   movie.trailer_link = tr_link

"""
def updateMovie(request,movie_id):
    categories=Category.objects.all()
    movie=Movie.objects.get(id=movie_id)
    if request.method=="POST":
        movie_name=request.POST["movie"]
        tr_link=request.POST['trailer_link']
        cate=request.POST['category']
        re_date=request.POST['release_date']
        if "poster" in request.FILES:
            poster=request.FILES["poster"]
            movie.poster=poster
        desc=request.POST["description"]
        rating=request.POST["rating"]
        category=Category.objects.get(id=cate)
        movie.movie=movie_name
        movie.trailer_link=tr_link
        movie.release_date=re_date
        movie.description=desc
        movie.rating=rating
        movie.category=category
        movie.save()
        return redirect("movie_detail",movie_id)
    return render(request,"update-movie.html",{"movie":movie,"categories":categories})

def movieDetail(request,movie_id):
    my_movie=Movie.objects.get(id=movie_id)
    return render(request,"movie-detail.html",{"movie":my_movie})