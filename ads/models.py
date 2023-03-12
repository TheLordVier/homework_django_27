from django.db import models


class Category(models.Model):
    """
    Клаcс-модели категория
    """
    name = models.TextField(max_length=200, unique=True)


class Ad(models.Model):
    """
    Клаcс-модели объявление
    """
    name = models.CharField(max_length=300)
    author = models.CharField(max_length=300)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=500)
    address = models.CharField(max_length=300)
    is_published = models.BooleanField(default=False)
