from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models

#Artist Model

class Artist(models.Model):
    stage_name = models.CharField(max_length=100,unique=True)
    social_link = models.URLField(max_length=300,blank=True, null=False)
  
    def approved_albums_num(self):
        return self.album_set.all().filter(is_approved=True).count()
    
    class Meta:
        ordering = ['stage_name']

    def __str__(self) :
        return self.stage_name



