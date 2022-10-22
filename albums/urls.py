from django.urls import path

from albums.views import AlbumCreate

urlpatterns =[
    path('create/',AlbumCreate),
]