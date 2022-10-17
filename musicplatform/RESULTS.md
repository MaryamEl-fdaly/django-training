>>> from artists.models import Artist
>>> from albums.models import Album
Queries and their result: 
1. create some artists
>>> a=Artist(stage_name='Hamaki',social_link='https://www.instagram.com/hamaki/')
>>> a.save()
>>> a1=Artist(stage_name='Tamer',social_link='https://www.instagram.com/tamerhosny/')                                  
>>> a1.save()
>>> a2=Artist(stage_name='Nancy',social_link='https://www.instagram.com/nancyajram/')
>>> a2.save()
>>> a3=Artist(stage_name='Maroon5',social_link='https://www.instagram.com/maroon5/')  
>>> a3.save()
>>> a4=Artist(stage_name='Ramy',social_link='https://www.instagram.com/ramygamalmusic/')
>>> a4.save()
2. list down all artists
>>> Artist.objects.all() 
Result: 
    <QuerySet [<Artist: Hamaki>, <Artist: Maroon5>, <Artist: Nancy>, <Artist: Ramy>, <Artist: Tamer>]>
3. list down all artists sorted by name
>>> Artist.objects.all().order_by('stage_name')
Result:
    <QuerySet [<Artist: Hamaki>, <Artist: Maroon5>, <Artist: Nancy>, <Artist: Ramy>, <Artist: Tamer>]>
4. list down all artists whose name starts with `a`
>>> Artist.objects.filter(stage_name__startswith='a')
Result:
    <QuerySet []>
    Note: Since there is no artists whose stage name start with a. After adding one more artist: 
    >>> a5=Artist(stage_name='Asala',social_link='https://www.instagram.com/asala/')         
    >>> a5.save()
    >>> Artist.objects.filter(stage_name__startswith='a')
Result:
    <QuerySet [<Artist: Asala>]>
5. create some albums and assign them to any artists
>>> import datetime
>>> from django.utils import timezone
>>> ab=Album(artist=Artist.objects.get(stage_name='Hamaki'),name='MaBlash',creation_datetime=datetime.datetime(2020,5,4,12,16),release_datetime=timezone.now(),cost=234000)
>>> ab.save()
>>> ab1=Album(artist=Artist.objects.get(stage_name='Maroon5'),name='Memories',creation_datetime=datetime.datetime(2022,5,7,2,16),release_datetime=timezone.now(),cost=5400000.9)
>>> ab1.save()
>>> ab2=Album(name='Yala',creation_datetime=datetime.datetime(2022,1,4,5,7),release_datetime=datetime.datetime(2022,1,20,10,00),cost=20000) 
>>> artist=Artist.objects.get(stage_name='Nancy')
>>> ab2.artist=artist
>>> ab2.save()
>>> artist1=Artist.objects.get(stage_name='Ramy')
>>> ab3=artist1.album_set.create(creation_datetime=datetime.datetime(2022,4,6,7,20),release_datetime=datetime.datetime(2022,4,25,4,2),cost=340003,name='Shaif Nafsk')
>>> ab4=Album(artist=Artist.objects.get(stage_name='Tamer'),name='Hdl3ny',creation_datetime=datetime.datetime(2021,2,7,21,16),release_datetime=datetime.datetime(2021,2,15,1,16),cost=41000.9)
>>> ab4.save()
>>> ab5=Album(artist=Artist.objects.get(stage_name='Tamer'),name='MshMohtam',creation_datetime=datetime.datetime(2022,10,7,21,16),release_datetime=datetime.datetime(2022,11,15,1,16),cost=21000.9)
>>> ab5.save()
6. get the latest released album
>>> Album.objects.latest('release_datetime')
Result:
   <Album: MshMohtam>
7. get all albums released before today
>>> Album.objects.filter(release_datetime__lt=datetime.date.today())
Result:
   <QuerySet [<Album: Yala>, <Album: Shaif Nafsk>, <Album: Hdl3ny>]>
8. get all albums released today or before but not after today
>>> Album.objects.filter(release_datetime__date__lte=datetime.date.today())
Note: The query gives error and I tried to solve it with no result. 
>>> Album.objects.filter(release_datetime__lte=datetime.date.today())
Note: this just prints the before today albums and not today.

9. count the total number of albums
>>> Album.objects.count()
Result:
    6
10. for each artist, list down all of his/her albums
>>> Album.objects.values('artist','name')     
Result:
    <QuerySet [{'artist': 1, 'name': 'MaBlash'}, {'artist': 4, 'name': 'Memories'}, {'artist': 3, 'name': 'Yala'}, {'artist': 5, 'name': 'Shaif Nafsk'}, {'artist': 2, 'name': 'Hdl3ny'}, {'artist': 2, 'name': 'MshMohtam'}]>

>>> list=[]
>>> for i in Album.objects.all():
...     list.append(i.artist)
...     list.append(i.name)
>>> print(list)
OR
>>> artists = Artist.objects.all()    
>>> for artist in artists:
...     artist.album_set.all()
Result:
    [<Artist: Hamaki>, 'MaBlash', <Artist: Maroon5>, 'Memories', <Artist: Nancy>, 'Yala', <Artist: Ramy>, 'Shaif Nafsk', <Artist: Tamer>, 'Hdl3ny', <Artist: Tamer>, 'MshMohtam']
11.  list down all albums ordered by cost then by name
>>> Album.objects.all().order_by('cost','name')  
Result:
    <QuerySet [<Album: Yala>, <Album: MshMohtam>, <Album: Hdl3ny>, <Album: MaBlash>, <Album: Shaif Nafsk>, <Album: Memories>]>

