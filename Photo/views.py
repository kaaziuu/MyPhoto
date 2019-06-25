from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .slug_generator import slug_generator
from .forms import addComment,AddPhoto
from .models import Photo,UserLike,Coments
from .scripts import deletePhoto
# Create your views here.

@login_required
def show_photo(request,slug):
    if request.is_ajax():
        # print('yes ajax')
        id = request.POST.get('id')
        fun = request.POST.get('f')
        photo = Photo.objects.filter(pk=id).first()
        if fun == 'like' or fun == 'unlike':

            is_like = UserLike.objects.filter(user=request.user, photo=photo)
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
                UserLike.objects.create(user=request.user, photo=photo)
                photo.like += 1
                photo.save()
        elif fun =='deletePhoto':
            deletePhoto(id)
            redirect('/')

        elif fun == 'comment':
            comment = request.POST.get('comment')
            Coments.objects.create(author=request.user, photo=photo, comment=comment)

        elif fun == 'deleteComment':
            author_use = request.POST.get('useAuthor')

            if author_use == 'false':
                Coments.objects.filter(pk=id).delete()
                
            else:
                author = request.POST.get('author')
                photoID = request.POST.get('photoID')
                all_com = Coments.objects.filter(author__username=author,photo__pk=int(photoID))
                all_com[int(id)].delete()



    form =  addComment()

    obj = Photo.objects.filter(slug=slug)
    photo_like = UserLike.objects.filter(user=request.user, photo=obj.first(), islike=True)

    com = Coments.objects.filter(photo__in=obj)
    # print(com)
    context = {
        'photo': obj.first(),
        'form': form,
        'comments': com,
        "toBottom": True
    }
    if len(photo_like) > 0:
        context['like'] = True
    else:
        context['like'] = False

    return render(request, 'photo.html', context)

@login_required
def add_photo(request):
    form = AddPhoto(request.POST or None, request.FILES or None)
    if form.is_valid():
        print(form.cleaned_data)
        obj = form.save(commit=False)
        obj.author = request.user
        ok = False
        while not ok:
            try:
                obj.slug = slug_generator()
                ok = True
            except:
                print('again')
        obj.save()
        return redirect('/u/'+request.user.username)

    context = {
        'form': form,
        "toBottom": True

    }
    return  render(request, 'add_photo.html', context)