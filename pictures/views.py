from django.shortcuts import render
from django.http import HttpResponse,Http404

# Create your views here.
def welcome(request):
    title = "Nelly's Gallery"
    return render(request,"pictures/pictures.html",{"title":title})