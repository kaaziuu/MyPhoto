from django.shortcuts import render
from  django.contrib.auth.models import User
from Photo.models import Photo, FollowedStatus
from .models import userData

# Create your views here.

def userPage(request, nick):
    if request.is_ajax():
        # print('test')
        fl_nick = request.POST.get('nick')
        print(fl_nick)
        fun = request.POST.get('f')
        # print(fun)
        if fun == 'follow':
            our_status = FollowedStatus.objects.filter(u1__username=fl_nick, u2=request.user)
            print(our_status)
            if len(our_status) > 0:
                our_status = our_status.first()
                if our_status.status == 0:
                    our_status.status = 2

                elif our_status.status == 1:
                    our_status.status = 3
                our_status.save()
            else:
                our_status = FollowedStatus.objects.filter(u1=request.user, u2__username=fl_nick)
                # print("---")
                # print(our_status)
                if len(our_status) > 0:
                    our_status = our_status.first()
                    if our_status.status == 0:
                        our_status.status = 1
                    elif our_status.status == 2:
                        our_status.status = 3
                    our_status.save()
                else:
                    u2 = User.objects.get(username=fl_nick)
                    # print(u2)
                    FollowedStatus.objects.create(u1=request.user, u2=u2, status=1)

        elif fun == 'unfollow':
            u2 = User.objects.get(username=fl_nick)
            print(u2)
            our_status = FollowedStatus.objects.filter(u1=u2, u2=request.user)
            print(our_status)
            if len(our_status) > 0:
                our_status = our_status.first()
                if our_status.status == 3:
                    our_status.status = 1

                elif our_status.status == 2:
                    our_status.status = 0
                our_status.save()

            else:
                our_status = FollowedStatus.objects.filter(u1=request.user, u2=u2)
                print(our_status)
                if len(our_status) > 0:
                    our_status = our_status.frist()
                    if our_status.status == 1:
                        our_status.status = 0
                    elif our_status.status == 3:
                        our_status.status = 2
                    our_status.save()
                else:
                    print('error')






    # print('test')
    Ifollow = False
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
            if status.u2 == request.user:
                Ifollow = True
        elif status.status == 2:
            ct_followers += 1
            if status.u2 == request.user:
                Ifollow = True
        elif status.status == 1:
            ct_following += 1

    followed_list = FollowedStatus.objects.filter(u2__username=nick)
    for status in followed_list:
        if status.status == 3:
            ct_following += 1
            ct_followers += 1
            if status.u1 == request.user:
                Ifollow = True
        elif status.status == 1:
            ct_followers += 1
            if status.u2 == request.user:
                Ifollow = True
        elif status.status == 2:
            ct_following += 1

    context = {
        'isPhoto': is_photo,
        'photos': objs,
        'user': userDatas,
        'following': ct_following,
        'followers': ct_followers,
        'nick': nick,
        'Ifollow': Ifollow
    }
    return render(request, 'userPage.html', context)
