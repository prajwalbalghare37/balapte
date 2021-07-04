from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Image

# Create your views here.

def galleryHome(request):
    images = Image.objects.all()
    for img in images:
        print(img.image.url)
    context = {
        'images': images,
    }
    return render(request, 'gallery/galleryHome.html', context)
