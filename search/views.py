from django.shortcuts import render
from user.models import userData
# Create your views here.

def search(request):
    query = request.GET.get('q',None)

    context = {}
    if query is not None:
        user_list = userData.object.all().search(query)
        context['userlist'] = user_list

    return render(request,'search.html',context)
