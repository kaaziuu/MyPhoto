from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Photo,UserLike
# Create your views here.

def show_photo(request,slug):



    obj = Photo.objects.filter(slug=slug)
    photo_like = UserLike.objects.filter(user=request.user, photo=obj.first(), islike=True)

    context = {
        'photo': obj.first()
    }
    if len(photo_like) > 0:
        context['like'] = True
    else:
        context['like'] = False

    return render(request, 'photo.html', context)
