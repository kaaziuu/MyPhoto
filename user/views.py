from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Photo.models import Photo, FollowedStatus
from .models import UserData
from .forms import ProfilePicterEdit,DescriptionEdit
from user import followi

# Create your views here.

@login_required
def userPage(request, nick):
    if request.is_ajax():
        followi.follow_and_unfollow(request,nick)

    user = User.objects.filter(username=nick)
    if len(user)== 0 :
        return redirect('/')

    I_follow = False

    objs = Photo.objects.filter(author__username=nick)
    user_datas = UserData.object.all().by_nick(nick)
    is_photo = False
    if len(user_datas) > 0:
        user_datas = user_datas.first()
        if user_datas.profilePicture:
            is_photo = True

    ct_following = 0
    ct_followers = 0
    followed_list = FollowedStatus.objects.filter(u1__username=nick)
    for status in followed_list:
        if status.status == 3:
            ct_following += 1
            ct_followers += 1
            if status.u2 == request.user:
                I_follow = True
        elif status.status == 2:
            ct_followers += 1
            if status.u2 == request.user:
                I_follow = True
        elif status.status == 1:
            ct_following += 1

    followed_list = FollowedStatus.objects.filter(u2__username=nick)
    for status in followed_list:
        if status.status == 3:
            ct_following += 1
            ct_followers += 1
            if status.u1 == request.user:
                I_follow = True
        elif status.status == 1:
            ct_followers += 1
            if status.u1 == request.user:
                I_follow = True
        elif status.status == 2:
            ct_following += 1

    context = {
        'isPhoto': is_photo,
        'photos': objs,
        'user': user_datas,
        'following': ct_following,
        'followers': ct_followers,
        'nick': nick,
        'Iollow': I_follow,
    }
    return render(request, 'user_page.html', context)

@login_required
def edit(request,nick):
    if request.user.username != nick:
        url = '/u/'+nick+'/edit'
        return redirect(url)
    if request.is_ajax():
        mod = request.POST.get('mode')

        if mod == 'des':
            print(mod)
            new_des = request.POST.get('des')
            data = UserData.object.by_nick(request.user.username)
            print(new_des)
            print(data)
            # data= data.first()
            data = data[0]
            data.description = new_des
            print(data)
            data.save()


    data = UserData.object.all().by_nick(nick)
    data = data.first()
    image_edit = ProfilePicterEdit(request.POST or None,request.FILES or None,instance=data)
    if image_edit.is_valid():
        image_edit.save()
        image_edit = ProfilePicterEdit()

    description_edit = DescriptionEdit(instance=data)
    image_edit = ProfilePicterEdit()

    context = {
        'data': data,
        'imageEdit': image_edit,
        'descriptionEdit': description_edit
    }
    return render(request,'edit_page.html',context)