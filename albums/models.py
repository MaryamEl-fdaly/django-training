from email.policy import default
from django.db import models
from artists.models import Artist
import datetime
from django.utils import timezone

# Album Model

class Album(models.Model):
    artist=models.ForeignKey(Artist,on_delete=models.CASCADE)
    name=models.CharField(max_length=100, default='New Album')
    creation_datetime = models.DateTimeField()
    release_datetime=models.DateTimeField(blank=False)
    cost=models.DecimalField(max_digits=10,decimal_places=2)
    # (1.Add a boolean field to the album model )
    is_approved=models.BooleanField(default=False)
    def __str__(self) :
        return self.name


