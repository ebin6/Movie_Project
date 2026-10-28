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


def updateMovie(request,movie_id):
    categories=Category.objects.all()
    movie=Movie.objects.get(id=movie_id)
    return render(request,"update-movie.html",{"movie":movie,"categories":categories})

def movieDetail(request,movie_id):
    my_movie=Movie.objects.get(id=movie_id)
    return render(request,"movie-detail.html",{"movie":my_movie})