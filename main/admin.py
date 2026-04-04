from django.contrib import admin
from .models import (
    Audio, Workbook, Article, Product, About,
    Book, GalleryPhoto, Film, MusicTrack
)

admin.site.register(Audio)
admin.site.register(Workbook)
admin.site.register(Article)
admin.site.register(Product)
admin.site.register(About)

# NEW MODELS FOR CLIENT'S EXTRA GEMS
admin.site.register(Book)
admin.site.register(GalleryPhoto)
admin.site.register(Film)
admin.site.register(MusicTrack)