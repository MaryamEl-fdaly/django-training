from email.policy import default
from django.db import models
from artists.models import Artist
import datetime
from django.utils import timezone

# Task 3: 
## 1.Instead of having an explicit `created_at` field in the `Album` model, inherit from [`TimeStampedModel`]
class TimeStampedModel(models.Model):
      creation_datetime = models.DateTimeField(auto_now_add=True)
      class Meta:
        abstract = True     
# Album Model

class Album(TimeStampedModel):
    artist=models.ForeignKey(Artist,on_delete=models.CASCADE)
    name=models.CharField(max_length=100, default='New Album')
    #creation_datetime = models.DateTimeField()
    release_datetime=models.DateTimeField(blank=False)
    cost=models.DecimalField(max_digits=10,decimal_places=2)
    # (1.Add a boolean field to the album model )
    is_approved=models.BooleanField(default=False)
    def __str__(self) :
        return self.name


