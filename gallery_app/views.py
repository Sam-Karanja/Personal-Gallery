from email import message
from unicodedata import category
from django.shortcuts import render

import photos
from .models import Image,Location
from .models import Category, Image, Location

# Create your views here.
def index(request):
    location = location.objects.all()
    photos = Image.current_images(location)
    return render(request,'index.html', {'photos':photos})


    
def search_results(request):
   locations = locations.objects.all()
   if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_images = Image.search_by_catgory(search_term)
        message = f"{search_term}"

   return render(request,'all-photos/search.html',{"message":message, "locations":locations,"photos":searched_images})
   


def location_results(request):
    location = Location.objects.all()
    photos = Image.current_images(location)

    if 'photo' in request.GET and request.GET["photo"]:
        search_location = request.GET.get("photo")
        found_location = Image.find_by_location(search_location)
        message = f"{search_location}"
        return render(request,'all-photos/location.html', {"photos":photos,"location":location,"message":message,"photos":found_location})
    else:
        message = "No suce Location"
        return render(request,'all-photos/location.html',{"message":message})

def photo(request,photo_id):
    photo = Image.objects.get(id=photo_id)
    return render(request,"all-photos/image.html",{"photo":photo}) 