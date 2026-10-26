from django.shortcuts import render
from movie.models import Category
# Create your views here.


def addMovie(request):
    categories=Category.objects.all()
    return render(request,"add-movie.html",{"categories":categories})