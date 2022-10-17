from dataclasses import field
from pyexpat import model
from django.contrib import admin
from .models import Album,Artist
from django import forms

# (4. without modifying the boolean field itself (modifying the form))
class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        # (4. help text that would show up under the previously mentioned boolean field)
        help_texts = {'is_approved':'Approve the album if its name is not explicit'}
        exclude=()
        

class InlineAlbum(admin.StackedInline):
    model = Album
    form = AlbumForm
    extra=1


class AlbumAdmin(admin.ModelAdmin):
    form = AlbumForm
    fields = ('artist','name','creation_datetime','release_datetime','cost','is_approved')
    # (3. The admin shouldn't be able to modify the creation time field on the album)
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('creation_datetime',)
        return self.readonly_fields

# (7.Allow the admin to create albums for the artist from from the artist's editing form)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [InlineAlbum]
    fields = ('stage_name','social_link')
    # (5. a column to show the number of approved albums for each artist)
    list_display = ('stage_name','approved_albums_num',)

# Registering Album and Artist models (2.Add all models you have so far to django admin)
admin.site.register(Album,AlbumAdmin)
admin.site.register(Artist,ArtistAdmin)
