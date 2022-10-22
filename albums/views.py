from django.shortcuts import render,redirect
from django.http import HttpRequest
from .forms import AlbumForm

# Create your views here.
def AlbumCreate(request):
    form = AlbumForm()
    if request.method =='POST':
            form = AlbumForm(request.POST)
            #4. For both forms, when the validation fails, the user should see errors
            if form.is_valid():
                form.save()  
    else:
        form = AlbumForm() 
    context={'form': form}
    return render(request,'album_create.html',context)

