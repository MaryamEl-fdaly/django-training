from django.urls import path

from artists.views import *

urlpatterns =[
    path('create/',ArtistCreate),
    path('',ListArtist),
]