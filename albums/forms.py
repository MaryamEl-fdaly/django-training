from dataclasses import fields
from django.forms import ModelForm, SelectDateWidget
from .models import Album
from django.contrib.admin.widgets import AdminSplitDateTime

#3. Create a form that allows a user to create an album 
class AlbumForm(ModelForm):
    class Meta:
        model=Album
        fields = ['artist','name','release_datetime','cost','is_approved']
     #   widgets = {
      #      'release_datetime':  AdminSplitDateTime(), 
       # }