from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Photo
# Create your views here.

def show_photo(request,slug):
    obj = Photo.objects.filter(slug=slug)
    print(obj)
    context = {
        'photo':obj.first()
    }

    return render(request,'photo.html',context)
