from django.shortcuts import render
from .models import (
    Audio, Workbook, Article, Product, About,
    Book, GalleryPhoto, Film, MusicTrack
)

# ====================== MAIN PAGES ======================
def portal(request):
    return render(request, 'portal.html')

def main_page(request):
    return render(request, 'main.html')

# ====================== EXISTING PAGES ======================
def radio_page(request):
    return render(request, 'radio.html', {'audios': Audio.objects.all().order_by('-date')})

def workbooks_page(request):
    return render(request, 'workbooks.html', {'workbooks': Workbook.objects.all()})

def teachings_page(request):
    return render(request, 'teachings.html', {'articles': Article.objects.all().order_by('-date')})

def shop_page(request):
    return render(request, 'shop.html', {'products': Product.objects.all()})

def about_page(request):
    return render(request, 'about.html', {'about': About.objects.first()})

def community_page(request):
    return render(request, 'community.html')

# ====================== NEW CLIENT PAGES ======================
def backstory_page(request):
    return render(request, 'backstory.html')

def response_to_windrush_page(request):
    return render(request, 'response_to_windrush.html')

def books_page(request):
    return render(request, 'books.html', {'books': Book.objects.all()})

def music_page(request):
    return render(request, 'music.html', {'music': MusicTrack.objects.all()})

def film_archive_page(request):
    return render(request, 'film_archive.html', {'films': Film.objects.all()})

def photo_gallery_page(request):
    return render(request, 'photo_gallery.html', {'photos': GalleryPhoto.objects.all()})

def merangel_art_page(request):
    return render(request, 'merangel_art.html')

def rainbows_end_page(request):
    return render(request, 'rainbows_end.html')