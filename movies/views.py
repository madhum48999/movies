from   django.http import HttpResponse
from django.shortcuts import render
from .models import Movie


def movies(request):
    data = Movie.objects.all()  
    return render(request, 'movies/movies.html',{'movies' : data})

def home(request):
    return HttpResponse("Welcome to the Movies App")

def detail(request, movie_id):
    data = Movie.objects.get(id=movie_id)
    return render(request, 'movies/detail.html', {'movie': data})