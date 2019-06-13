from django.shortcuts import render

from .forms import addComment
from .models import Photo,UserLike,Coments
# Create your views here.

def show_photo(request,slug):
    if request.is_ajax():
        # print('yes ajax')
        id = request.POST.get('id')
        fun = request.POST.get('f')
        photo = Photo.objects.filter(pk=id).first()
        # print(fun)
        if fun =='like' or fun=='unlike':
            is_like = UserLike.objects.filter(user=request.user,photo=photo)
            if len(is_like) > 0:
                is_like = is_like.first()
                if getattr(is_like, 'islike'):
                    is_like.islike = False
                    photo.like -= 1
                else:
                    is_like.islike = True
                    photo.like += 1

                photo.save()
                is_like.save()

            else:
                UserLike.objects.create(user=request.user, photo = photo)
                photo.like += 1
                photo.save()

        elif fun == 'comment':
            comment = request.POST.get('comment')
            Coments.objects.create(author=request.user, photo=photo, comment=comment)

        elif fun == 'deleteComment':
            author_use = request.POST.get('useAuthor')

            if author_use == 'false':
                Coments.objects.filter(pk=id).delete()
                
            else:
                author = request.POST.get('author')
                all_com = Coments.objects.filter(author__username=author)
                all_com[int(id)].delete()


    form =  addComment()



    obj = Photo.objects.filter(slug=slug)
    photo_like = UserLike.objects.filter(user=request.user, photo=obj.first(), islike=True)

    com = Coments.objects.filter(photo__in=obj)
    # print(com)
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

