from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.hashers import make_password

""" 3 models: Note, Tag, User """

class NoteStackUser(AbstractBaseUser):
    """User model"""
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    raw_password = models.CharField(max_length=50)
    is_staff = models.BooleanField()
    password = make_password(str(raw_password)) # Enables password hashing


class Tag(models.Model):
    """Tag model"""
    caption = models.CharField(max_length=50)


class Note(models.Model):
    """Note model"""
    user = models.ForeignKey(NoteStackUser, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    text = models.TextField()
    



