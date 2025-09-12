from django.shortcuts import render

from rest_framework import viewsets

from .models import NoteStackUser, Note, Tag
from .serializers import NoteSerializer, NoteStackUserSeriazlizer, TagSerializer

"""Views to enable displaying the notes. One for each model"""


class NoteStackUserViewSet(viewsets.ModelViewSet):
    queryset = NoteStackUser.objects.all()
    serializer_class = NoteStackUserSeriazlizer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    