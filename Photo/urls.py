from django.urls import path
from .views import *

urlpatterns =[
    path('<str:slug>/',show_photo)
]