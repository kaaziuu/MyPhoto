from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Photo.models import Photo, FollowedStatus
from .models import userData
from .forms import ProfilePicterEdit,DescriptionEdit

# Create your views here.

@login_required
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


    user = User.objects.filter(username=nick)
    if len(user)== 0 :
        return redirect('/')

    Ifollow = False

    objs = Photo.objects.filter(author__username=nick)
    userDatas = userData.object.all().by_nick(nick)
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
            if status.u1 == request.user:
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
    return render(request, 'user_page.html', context)

@login_required
def edit(request,nick):
    if request.user.username != nick:
        url = '/u/'+nick+'/edit'
        return redirect(url)
    data = userData.object.all().by_nick(nick)
    data = data.first()
    image_edit = ProfilePicterEdit(request.POST or None, request.FILES or None,instance=data)
    if image_edit.is_valid():
        image_edit.save()
        image_edit = ProfilePicterEdit()

    description_edit = DescriptionEdit(request.POST or None,instance=data)
    if description_edit.is_valid():
        description_edit.save()
        description_edit = DescriptionEdit(instance=data)

    context = {
        'data': data,
        'imageEdit': image_edit,
        'descriptionEdit': description_edit
    }
    return render(request,'edit_page.html',context)