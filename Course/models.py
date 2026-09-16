from django.db import models

# Create your models here.
class Playlist(models.Model):
    youtube_id = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=3000, blank=True)
    thumbnail = models.URLField(max_length=500, blank=True, null=True)
    video_count = models.IntegerField(default=0)
    last_synced = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.youtube_id

class Video(models.Model):
    youtube_id = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=3000, blank=True)
    thumbnail = models.URLField(max_length=500, blank=True, null=True)
    duration = models.PositiveIntegerField(blank=True, null=True)
    published_at = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.youtube_id

class VideoPosition(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    position = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class UserPlaylist(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    is_favorite = models.BooleanField(default=False)
    last_viewed_video = models.ForeignKey(Video, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
