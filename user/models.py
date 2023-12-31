from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None

    avatar = models.ImageField(verbose_name="аватар", blank=True, null=True)
    email = models.EmailField(verbose_name='почта', unique=True)
    telephone = models.CharField(max_length=15, verbose_name="telephone", blank=True, null=True)
    country = models.ForeignKey('Countries', on_delete=models.SET_NULL, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Countries(models.Model):
    title = models.CharField(max_length=15, verbose_name="Country", unique=True)

    def __str__(self):
        return self.title
