from Photo.models import FollowedStatus
from django.contrib.auth.models import User

def follow_and_unfollow(request,nick=''):
    if nick == '':
        nick = request.POST.get('nick')
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