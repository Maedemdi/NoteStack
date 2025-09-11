from django.shortcuts import render

from rest_framework import viewsets

from .models import NoteStackUser, Note, Tag
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    