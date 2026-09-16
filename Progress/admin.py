from django.contrib import admin
from .models import VideoProgress

class VideoProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'video', 'last_watched_position','is_completed', 'created', 'modified')

# Register your models here.
admin.site.register(VideoProgress, VideoProgressAdmin)