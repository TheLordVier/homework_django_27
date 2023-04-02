from django.contrib.auth.models import AbstractUser
from django.db import models


class Location(models.Model):
    """
    Клаcс-модели местонахождение
    """
    name = models.CharField("Название", max_length=200, unique=True)
    lat = models.DecimalField("Широта", max_digits=8, decimal_places=6, null=True, blank=True)
    lng = models.DecimalField("Долгота", max_digits=8, decimal_places=6, null=True, blank=True)

    class Meta:
        verbose_name = 'Местонахождение'
        verbose_name_plural = 'Местонахождения'

    def __str__(self):
        return self.name


class User(AbstractUser):
    """
    Клаcс-модели пользователь
    """
    MEMBER = "member"
    MODERATOR = "moderator"
    ADMIN = "admin"
    ROLES = [
        ("member", "Пользователь"),
        ("moderator", "Модератор"),
        ("admin", "Админ"),
    ]

    role = models.CharField(max_length=9, choices=ROLES, default="member")
    age = models.PositiveSmallIntegerField(null=True)
    location = models.ManyToManyField(Location)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
