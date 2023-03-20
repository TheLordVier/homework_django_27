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


class UserRoles(models.TextChoices):
    """
    Клаcс-модели роль пользователя
    """
    MEMBER = "member", "Пользователь"
    MODERATOR = "moderator", "Модератор"
    ADMIN = "admin", "Админ"


class User(models.Model):
    """
    Клаcс-модели пользователь
    """
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=150)
    username = models.CharField("Никнейм", max_length=100, unique=True)
    password = models.CharField("Пароль", max_length=200)
    role = models.CharField(choices=UserRoles.choices, max_length=9)
    age = models.PositiveSmallIntegerField()
    location = models.ManyToManyField(Location)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def __str__(self):
        return self.username
