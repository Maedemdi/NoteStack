from rest_framework import serializers
from .models import NoteStackUser, Note, Tag


class NoteStackUserSeriazlizer(serializers.ModelSerializer):
    class Meta:
        model = NoteStackUser
        fields = '__all__'
        exclude = ('password', 'raw_password')


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'