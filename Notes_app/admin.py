from django.contrib import admin

from .models import NoteStackUser, Note, Tag

"""Registering models into admin panel"""

class NoteAdmin(admin.ModelAdmin):
    """Customized display of notes in admin panel"""
    list_display = ('text', 'user__username')

admin.site.register(Note, NoteAdmin)
admin.site.register(Tag)
admin.site.register(NoteStackUser)

