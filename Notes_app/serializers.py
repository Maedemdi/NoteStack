from rest_framework import serializers
from .models import NoteStackUser, Note, Tag

"""Serializing data, one for each associated model"""


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = NoteStackUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


    def create(self, validated_data):
        password = validated_data.pop("password")
        user = NoteStackUser.objects.create_user(
            password=password,
            **validated_data
        )
        return user



# class NoteStackUserSeriazlizer(serializers.ModelSerializer):
#     class Meta:
#         model = NoteStackUser
#         fields = '__all__'


# class TagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tag
#         fields = '__all__'