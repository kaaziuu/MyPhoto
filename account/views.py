from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    login,
    logout as dj_logout
)
from .forms import *
from user.models import userData

# Create your views here.

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user =  authenticate(username=username,password=password)

        login(request,user)
        if next:
            redirect(next)

        return redirect('/u/kaziu')

    context = {
        'form':form,
        'w':'login'
    }
    return render(request,'tem.html',context)


def logout(request):
    dj_logout(request)
    return redirect('/accounts/login/')

def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username,password=password)
        login(request,new_user)

        if next:
            return redirect(next)

        new_data = userData()
        new_data.user = request.user
        new_data.save()

        return redirect('/')

    context = {
        'form': form,
        'w': 'register'
    }
    return render(request,'tem.html',context)



