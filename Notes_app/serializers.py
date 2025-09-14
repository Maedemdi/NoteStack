from rest_framework import serializers
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