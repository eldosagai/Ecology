from django.contrib import admin
from .models import Article, ArticleImage, Event, EventImage
# Register your models here.

class ArticleInline(admin.StackedInline):
    model = ArticleImage
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','id']
    inlines = [ArticleInline]

@admin.register(ArticleImage)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['article','image']

class EventInline(admin.StackedInline):
    model = EventImage
    extra = 1

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name','organization','type','place','date','id']
    inlines = [EventInline]

@admin.register(EventImage)
class EventImageAdmin(admin.ModelAdmin):
    list_display = ['event','image']