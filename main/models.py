from django.db import models
from django.utils.timezone import now
from django.utils.text import slugify # Required for generating slugs

class Audio(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True, blank=True, null=True) # Added slug
    order = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)
    audio_file = models.FileField(upload_to='audios/')
    date = models.DateField(default=now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self): return self.title

class Workbook(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True, blank=True, null=True) # Added slug
    description = models.TextField(blank=True)
    pdf_file = models.FileField(upload_to='workbooks/')
    cover_image = models.ImageField(upload_to='covers/', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self): return self.title

class Chapter(models.Model):
    workbook = models.ForeignKey(Workbook, related_name='chapters', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="Title", db_index=True)
    pages = models.CharField(max_length=50, help_text="e.g., 1-10", verbose_name="Pages")
    start_page = models.PositiveIntegerField(default=1, verbose_name="Start Page")
    end_page = models.PositiveIntegerField(default=1, verbose_name="End Page")
    order = models.PositiveIntegerField(default=0)
    def __str__(self): return f"{self.workbook.title} - {self.title}"

class Article(models.Model):
    """Used for Teachings and the Windrush Poems"""
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True, blank=True, null=True) # Added slug
    content = models.TextField()
    date = models.DateField(default=now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self): return self.title

class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True, blank=True, null=True) # Added slug
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name) # Uses 'name' instead of 'title'
        super().save(*args, **kwargs)

    def __str__(self): return self.name

class Film(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True, blank=True, null=True) # Added slug
    video_file = models.FileField(upload_to='films/', blank=True)
    youtube_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to='films/', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self): return self.title

class About(models.Model):
    title = models.CharField(max_length=100, default="One Love Nation")
    content = models.TextField()
    def __str__(self): return self.title
    
class Book(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True, blank=True, null=True) # Added slug
    author = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    cover = models.ImageField(upload_to='books/', blank=True)
    pdf = models.FileField(upload_to='books/', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self): return self.title

class GalleryPhoto(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True)
    def __str__(self): return self.title

class MusicTrack(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True, blank=True, null=True) # Added slug
    artist = models.CharField(max_length=100, blank=True)
    audio_file = models.FileField(upload_to='music/')
    cover_image = models.ImageField(upload_to='music_covers/', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self): return self.title