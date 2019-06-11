from django.shortcuts import render
from Photo.models import Photo

# Create your views here.

def userPage(request,nick):
    objs = Photo.objects.filter(author__username=nick)
    context = {
        'photos' : objs
    }
    return render(request,'userPage.html',context)
