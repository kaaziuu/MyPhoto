from django.shortcuts import render
from Photo.models import Photo,FollowedStatus,UserLike

def main_view(request):
    if request.is_ajax():
        # print('yes ajax')
        id = request.POST.get('id')
        # fun = request.POST.get('f')

        photo = Photo.objects.filter(pk=id).first()
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
            # print(photo.like)

    like_obj = UserLike.objects.filter(user=request.user,islike=True)

    followed_people = []
    us = FollowedStatus.objects.filter(u1=request.user)
    for  u in us:
        if u.status == 1 or u.status == 3:
            followed_people.append(u.u2)

    us = FollowedStatus.objects.filter(u2=request.user)

    for u in us:
        if u.status == 2 or u.status == 3 and u.u1 not in followed_people:
            followed_people.append(u.u1)

    followed_people.append(request.user)

    obj = Photo.objects.filter(author__in=followed_people)

    tmp = []

    for o in like_obj:
        tmp.append(o.photo)

    context = {
        'photos': obj,
        'like': tmp
    }

    return render(request, 'main/front.html', context)



