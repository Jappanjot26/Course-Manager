from django.contrib import admin
from .models import Note
# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'video', 'timestamp', 'created', 'modified')

admin.site.register(Note, NoteAdmin)