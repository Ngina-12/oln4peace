from django.shortcuts import render
from .models import (
    Audio, Workbook, Article, Product, About,
    Book, GalleryPhoto, Film, MusicTrack
)

# HELPER: Reduces DB load by fetching only necessary fields
def portal(request): return render(request, 'portal.html')
def main_page(request): return render(request, 'main.html')

def radio_page(request): 
    # Optimized for the 'Long Version' SVG hotspots (14 shows)
    # Fetches only ID and audio path to keep the server light
    audios = Audio.objects.only('id', 'audio_file').order_by('id')[:14]
    return render(request, 'radio-shows.html', {'audios': audios})

def teachings_page(request): 
    # Fetches only summary info; prevents loading full article text on the list page
    articles = Article.objects.only('id', 'title', 'date').order_by('-date')
    return render(request, 'teachings.html', {'articles': articles})

def music_page(request): 
    # Optimized for SVG music card performance
    music = MusicTrack.objects.only('id', 'title', 'audio_file')
    return render(request, 'music.html', {'music': music})

def photo_gallery_page(request): 
    # Only pull the image reference, not the metadata
    photos = GalleryPhoto.objects.only('id', 'image')
    return render(request, 'photo_gallery.html', {'photos': photos})

# Standard pages (keeping logic minimal as requested)
def companion_workbooks_page(request): return render(request, 'companion workbooks.html', {'companion_workbooks': Workbook.objects.all()})
def shop_page(request): return render(request, 'shop.html', {'products': Product.objects.all()})
def about_page(request): return render(request, 'about.html', {'about': About.objects.first()})
def community_page(request): return render(request, 'community.html')
def backstory_page(request): return render(request, 'backstory.html')
def response_to_windrush_page(request): return render(request, 'response_to_windrush.html')
def books_page(request): return render(request, 'books.html', {'books': Book.objects.all()})
def film_archives_page(request): return render(request, 'film_archive.html', {'films': Film.objects.all()})
def merangel_art_page(request): return render(request, 'merangel_art.html')
def rainbows_end_page(request): return render(request, 'rainbows_end.html')
def response_to_windrush_index_page(request): return render(request, 'response_to_windrush_index.html')
def response_to_windrush_youtubepoems_page(request): return render(request, 'response_to_windrush_youtubepoems.html')