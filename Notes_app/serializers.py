from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import NoteStackUser, Note, Tag

"""Serializing data"""


class NoteSerializer(serializers.ModelSerializer):
    """Enables serializing and submitting notes"""
    user = serializers.SlugRelatedField(read_only=True, slug_field="username")
    tags = serializers.SlugRelatedField(many=True,
                                        slug_field="caption",
                                        queryset=Tag.objects.all())

    class Meta:
        model = Note
        fields = ('id', 'user', 'title', 'text', 'tags')
        read_only_fields = ('user',)


class SignUpSerializer(serializers.ModelSerializer):
    """Enables signing the user up"""
    password = serializers.CharField(write_only=True,
                                     min_length=8,
                                     style={'input_type': 'password',
                                            'placeholder': 'Password'})

    class Meta:
        model = NoteStackUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = NoteStackUser.objects.create_user(
            password=password,
            **validated_data
        )
        return user


class LoginSerializer(serializers.Serializer):
    """Enables user login"""
    username = serializers.CharField()
    password = serializers.CharField(write_only=True,
                                     style={'input_type': 'password',
                                            'placeholder': 'Password'})

    def validate(self, data):
        user = authenticate(
            username=data.get("username"),
            password=data.get("password")
        )
        if not user:
            raise serializers.ValidationError("Invalid username or password.")
        if not user.is_active:
            raise serializers.ValidationError("User account is disabled.")
        data["user"] = user
        return data
