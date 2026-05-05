from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import (
    portal, main_page,
    radio_page, companion_workbooks_page, teachings_page, shop_page, about_page, community_page,
    backstory_page, response_to_windrush_page, books_page, music_page,
    film_archives_page, photo_gallery_page, merangel_art_page, rainbows_end_page,
    response_to_windrush_index_page,
    response_to_windrush_youtubepoems_page
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portal, name='portal'),
    path('main/', main_page, name='main'),

    path('radio-shows/', radio_page, name='radio-shows'),
    path('companion-workbooks/', companion_workbooks_page, name='companion_workbooks'),
    path('teachings/', teachings_page, name='teachings'),
    path('shop/', shop_page, name='shop'),
    path('about/', about_page, name='about'),
    path('community/', community_page, name='community'),

    path('backstory/', backstory_page, name='backstory'),
    path('response-to-windrush/', response_to_windrush_page, name='response_to_windrush'),
    path('response-to-windrush-index/', response_to_windrush_index_page, name='response_to_windrush_index'),
    
    path('response-to-windrush-youtubepoems/', response_to_windrush_youtubepoems_page, name='response_to_windrush_youtubepoems'),

    path('books/', books_page, name='books'),
    path('music/', music_page, name='music'),
    path('film_archives/', film_archives_page, name='film_archives'),
    path('photo-gallery/', photo_gallery_page, name='photo_gallery'),
    path('merangels-art/', merangel_art_page, name='merangel_art'),
    path('rainbows-end/', rainbows_end_page, name='rainbows_end'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)