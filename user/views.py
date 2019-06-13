from django.shortcuts import render
from Photo.models import Photo,FollowedStatus
from .models import userData

# Create your views here.

<<<<<<< Updated upstream
def userPage(request,nick):
=======
def userPage(request, nick):
    if request.is_ajax():
        fl_nick = request.POST.get('nick')
        fun = request.POST.get('f')
        if fun == 'follow':
            our_status = FollowedStatus.objects.filter(u1__username=nick, u2=request.user)
            if len(our_status) > 0:
                our_status = our_status.first()
                if our_status.status == 0:
                    our_status.status = 2

                elif our_status.status == 1:
                    our_status.status = 3
                our_status.save()
            else:
                our_status = FollowedStatus.objects.filter(u1=request.user, u2__username=nick)

                if len(our_status) > 0:
                    our_status = our_status.first()
                    if our_status.status == 0:
                        our_status.status = 1
                    elif our_status.status == 2:
                        our_status.status = 3
                    our_status.save()
                else:
                    u2 = User.objects.get(username=nick)
                    FollowedStatus.objects.create(u1=request.user, u2=u2, status=1)

        elif fun == 'unfollow':

            # I don't know why i can't user fl_nick
            our_status = FollowedStatus.objects.filter(u1__username=nick, u2=request.user)
            if len(our_status) > 0:
                our_status = our_status.first()
                if our_status.status == 3:
                    our_status.status = 1

                elif our_status.status == 2:
                    our_status.status = 0
                our_status.save()

            else:
                our_status = FollowedStatus.objects.filter(u1=request.user, u2__username=nick)
                if len(our_status) > 0:
                    our_status = our_status.first()
                    if our_status.status == 1:
                        our_status.status = 0
                    elif our_status.status == 3:
                        our_status.status = 2
                    our_status.save()
                else:
                    print('error')

    Ifollow = False
>>>>>>> Stashed changes
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
