from rest_framework import serializers
from .models import NoteStackUser, Note, Tag

"""Serializing data, one for each associated model"""

class NoteStackUserSeriazlizer(serializers.ModelSerializer):
    class Meta:
        model = NoteStackUser
        fields = '__all__'
        exclude = ('password')


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'