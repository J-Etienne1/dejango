

from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    # /music/
    path('', views.index, name='index'),

    # /music/71


def detail(request, album_id):
    return HttpResponse("<h2> Details for Album ID: " + str(album_id) + "</2h>")
]