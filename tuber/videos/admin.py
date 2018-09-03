from django.contrib import admin
from .models import Video, Flipbook, Actor

# Register your models here.
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'channel', 'rating', 'views']
    list_filter = ['rating', 'views']
    search_fields = ['title', 'channel']
	#list_per_page = 25

class FlipbookAdmin(admin.ModelAdmin):
    list_display = ['video', 'images']
    search_fields = ['video']
	#list_per_page = 25

class ActorAdmin(admin.ModelAdmin):
    list_display = ['video', 'actors']
    search_fields = ['actors']
	#list_per_page = 25

admin.site.register(Video, VideoAdmin)
admin.site.register(Flipbook, FlipbookAdmin)
admin.site.register(Actor, ActorAdmin)