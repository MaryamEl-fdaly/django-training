from dataclasses import fields
from django.forms import ModelForm, SelectDateWidget
from .models import Artist
from django.contrib.admin.widgets import AdminSplitDateTime

#2. Create a form that allows a user to create an artist

class ArtistForm(ModelForm):
    class Meta:
        model=Artist
        fields = '__all__'