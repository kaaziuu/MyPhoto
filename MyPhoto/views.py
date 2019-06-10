from django.shortcuts import render
from Photo.models import Photo,FollowedStatus,UserLike

def main_view(request):
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


