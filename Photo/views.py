from django.shortcuts import render

from .forms import addComment
from .models import Photo,UserLike,Coments
# Create your views here.

def show_photo(request,slug):
    form =  addComment(request.POST or None)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.author = request.user
        new_comment.photo = Photo.objects.filter(slug=slug).first()
        new_comment.save()
        form = addComment()


    obj = Photo.objects.filter(slug=slug)
    photo_like = UserLike.objects.filter(user=request.user, photo=obj.first(), islike=True)

    com = Coments.objects.filter(photo__in=obj)
    print(com)
    context = {
        'photo': obj.first(),
        'form': form,
        'comments': com
    }
    if len(photo_like) > 0:
        context['like'] = True
    else:
        context['like'] = False

    return render(request, 'photo.html', context)

