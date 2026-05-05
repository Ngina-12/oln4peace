from django.contrib import admin
from .models import (
    Audio, Workbook, Article, Product, About,
    Book, GalleryPhoto, Film, MusicTrack, Chapter
)

class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 1
    fields = ('title', 'pages', 'start_page', 'end_page', 'order')

@admin.register(Workbook)
class WorkbookAdmin(admin.ModelAdmin):
    inlines = [ChapterInline]
    list_display = ('title',)

admin.site.register(Audio)
admin.site.register(Article)
admin.site.register(Product)
admin.site.register(About)
admin.site.register(Book)
admin.site.register(GalleryPhoto)
admin.site.register(Film)
admin.site.register(MusicTrack)
admin.site.register(Chapter)