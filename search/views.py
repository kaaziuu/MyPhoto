from django.shortcuts import render
from user.models import UserData
from Photo.models import FollowedStatus,Photo,UserLike
from user import followi

# Create your views here.


def search(request):
    template = 'user_search.html'
    if request.is_ajax():
        if request.POST.get('f') == 'follow' or request.POST.get('f') == 'unfollow':
            followi.follow_and_unfollow(request)
        elif request.POST.get('f') == 'like' or request.POST.get('f') == 'unlike':
            id = request.POST.get('id')
            photo = Photo.objects.filter(pk=id).first()
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
                template = 'main/front.html'

    query = request.GET.get('q', None)
    context = {}
    if query is not None:
        if query[0] == '#':
            template = 'main/front.html'
            photos = Photo.objects.filter(description__icontains = query)
            context['photos'] = photos
            like_obj = UserLike.objects.filter(user=request.user, islike=True)
            tmp = []

            for o in like_obj:
                tmp.append(o.photo)
            context['like'] = tmp
        else:
            template = 'search/user_search.html'
            user_list = UserData.object.all().search(query)
            context['userlist'] = user_list
            i_follow = []
            for user in user_list:
                tmp = FollowedStatus.objects.filter(u1=request.user, u2=user.user)
                if len(tmp) > 0:
                    tmp = tmp[0]
                    if tmp.status == 3 or tmp.status == 1:
                        i_follow.append(user)
                else:
                    tmp = FollowedStatus.objects.filter(u1=user.user, u2=request.user)
                    if len(tmp) > 0:
                        tmp = tmp[0]
                        if tmp.status == 3 or tmp.status == 2:
                            i_follow.append(user)

            context['following'] = i_follow


        print(context)
    return render(request, template, context)
