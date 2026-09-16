from django.db import models

# Create your models here.
class VideoProgress(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    video = models.ForeignKey('Course.Video', on_delete=models.CASCADE)
    last_watched_position = models.PositiveIntegerField(default=0)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)