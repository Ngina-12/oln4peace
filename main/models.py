from django.db import models
from django.utils.timezone import now

class Audio(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    audio_file = models.FileField(upload_to='audios/')
    date = models.DateField(default=now)
    def __str__(self): return self.title

class Workbook(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    pdf_file = models.FileField(upload_to='workbooks/')
    cover_image = models.ImageField(upload_to='covers/', blank=True)
    def __str__(self): return self.title

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(default=now)
    def __str__(self): return self.title

class Product(models.Model):  # Shop - empty until admin adds
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/', blank=True)
    stock = models.IntegerField(default=10)
    def __str__(self): return self.name

class About(models.Model):
    title = models.CharField(max_length=100, default="One Love Nation")
    content = models.TextField()
    def __str__(self): return self.title
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    cover = models.ImageField(upload_to='books/', blank=True)
    pdf = models.FileField(upload_to='books/', blank=True)
    def __str__(self): return self.title

class GalleryPhoto(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True)
    date = models.DateField(default=now)
    def __str__(self): return self.title

class Film(models.Model):
    title = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='films/', blank=True)
    youtube_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to='films/', blank=True)
    def __str__(self): return self.title

class MusicTrack(models.Model):
    title = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to='music/')
    description = models.TextField(blank=True)
    def __str__(self): return self.title