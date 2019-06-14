from django.urls import path
from .views import *

urlpatterns = [

    path('<str:nick>', userPage),
    path('<str:nick>/edit/', edit),

]