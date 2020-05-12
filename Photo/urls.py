from django.urls import path
from .views import *

urlpatterns =[
    path('<str:slug>/',show_photo),
    path('<str:slug>/edit/',show_photo),
    path('a/',add_photo),
    path("rm/", remove_photo),
]