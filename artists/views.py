from django.shortcuts import render,redirect
from django.http import HttpRequest
from .forms import ArtistForm
from .models import Artist

# Create your views here.
def ArtistCreate(request):
    form = ArtistForm()
    if request.method =='POST':
        form = ArtistForm(request.POST)
        #4. For both forms, when the validation fails, the user should see errors
        if form.is_valid():
            form.save()
    else:
        form = ArtistForm() 
    context={'form': form}
    return render(request,'artist_create.html',context)

## 5. Create a template view that lists all the albums grouped by each artist
def ListArtist(request):
    artists = Artist.objects.all().order_by('id')
    all_artists=[]
    for i in artists:
        artist_albums=i.album_set.all()
        item_list={
            'id':i.id,
            'stage_name':i.stage_name,
            'social_link':i.social_link,
            'albums':artist_albums,
        }
        all_artists.append(item_list)
    context= {'all': all_artists}
    return render(request, 'artists.html',context)
