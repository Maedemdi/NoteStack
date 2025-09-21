from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
""" 3 models: Note, Tag, User, User manager """


class NoteStackUserManager(BaseUserManager):
    """User manager"""

    def normalize_email(self, email):
        """Lowercase the entire email."""
        email = super().normalize_email(email)
        return email.lower() if email else None

    def create_user(self, username, first_name, last_name, email, password):
        if not username:
            raise ValueError("Users must have a username.")
        if not email:
            raise ValueError("Users must have an email address.")
        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, email, password):
        user = self.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class NoteStackUser(AbstractBaseUser, PermissionsMixin):
    """User model"""

    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name", "last_name", "email"]

    objects = NoteStackUserManager()

    class Meta:
        verbose_name_plural = 'NoteStack Users'


class Tag(models.Model):
    """Tag model"""

    caption = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.caption


class Note(models.Model):
    """Note model"""

    title = models.CharField(max_length=150, null=True)
    text = models.TextField()
    user = models.ForeignKey(NoteStackUser, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
