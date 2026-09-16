from django.contrib import admin
from .models import Playlist, Video, VideoPosition, UserPlaylist
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('youtube_id', 'video_count', 'created', 'modified')

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'modified')

class VideoPositionAdmin(admin.ModelAdmin):
    list_display = ('playlist', 'video', 'position', 'created', 'modified')

class UserPlaylistAdmin(admin.ModelAdmin):
    list_display = ('user', 'playlist', 'is_favorite', 'last_viewed_video', 'created', 'modified')

# Register your models here.
admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(VideoPosition, VideoPositionAdmin)
admin.site.register(UserPlaylist, UserPlaylistAdmin)
