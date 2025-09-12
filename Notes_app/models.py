from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password

""" 3 models: Note, Tag, User """


# class NoteStackUserManager(BaseUserManager):
#     """Manager required for authentication"""
#     pass 


class NoteStackUser(AbstractBaseUser):
    """User model"""
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField()
    email = models.EmailField()
    is_staff = models.BooleanField()
    password = make_password(str(password)) # Enables password hashing

    USERNAME_FIELD = "username"

    class Meta: 
        verbose_name_plural = 'NoteStack Users'


class Tag(models.Model):
    """Tag model"""
    caption = models.CharField(max_length=50)

    def __str__(self):
        return self.caption


class Note(models.Model):
    """Note model"""
    user = models.ForeignKey(NoteStackUser, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    text = models.TextField()
    



