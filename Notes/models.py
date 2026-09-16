from django.db import models

# Create your models here.
class Note(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    video = models.ForeignKey('Course.Video', on_delete=models.CASCADE)
    content = models.TextField(max_length=5000)
    timestamp = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)