from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Photo
# Create your views here.

def photos(request):
    title = "Nelly's Gallery"
    photos = Photo.photos()
    return render(request,"pictures/pictures.html",{"title":title,"photos":photos})