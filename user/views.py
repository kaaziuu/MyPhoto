from django.shortcuts import render
from Photo.models import Photo,FollowedStatus
from .models import userData

# Create your views here.

def userPage(request,nick):
    objs = Photo.objects.filter(author__username=nick)
    userDatas = userData.objects.filter(user__username=nick)
    is_photo = False
    if len(userDatas) > 0:
        userDatas = userDatas.first()
        if userDatas.profilePicture:
            is_photo = True

    ct_following = 0
    ct_followers = 0
    followed_list = FollowedStatus.objects.filter(u1__username=nick)
    for status in followed_list:
        if status.status == 3:
            ct_following += 1
            ct_followers += 1
        elif status.status ==  2:
            ct_followers += 1
        elif status.status == 1:
            ct_following += 1

    followed_list = FollowedStatus.objects.filter(u2__username=nick)
    for status in followed_list:
        if status.status == 3:
            ct_following += 1
            ct_followers += 1
        elif status.status ==  1:
            ct_followers += 1
        elif status.status == 2:
            ct_following += 1


    context = {
        'isPhoto' : is_photo,
        'photos' : objs,
        'user' : userDatas,
        'following' : ct_following,
        'followers' : ct_followers,
        'nick' : nick
    }
    return render(request,'userPage.html',context)
