from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Photo,Category,Location
# Create your views here.

def photos(request):
    title = "Nelly's Gallery"
    photos = Photo.photos()
    return render(request,"pictures/pictures.html",{"title":title,"photos":photos})

def search_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos = Photo.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'pictures/search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'pictures/search.html',{"message":message})