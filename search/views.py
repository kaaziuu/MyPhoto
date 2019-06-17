from django.shortcuts import render
from user.models import userData
from Photo.models import FollowedStatus,Photo
from user import followi
# Create your views here.


def search(request):
    if request.is_ajax():
        followi.follow_and_unfollow(request)

    query = request.GET.get('q', None)
    context = {}
    tempate = 'user_search.html'
    if query is not None:
        if query[0] == '#':
            tempate = 'main/front.html'
            photos = Photo.objects.filter(description__icontains = query)
            context['photos'] = photos
        else:
            tempate = 'search/user_search.html'
            user_list = userData.object.all().search(query)
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
    return render(request, tempate, context)
