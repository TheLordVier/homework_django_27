from django.core.validators import MinLengthValidator
from django.db import models

from users.models import User


class Category(models.Model):
    """
    Клаcс-модели категория
    """
    name = models.TextField(max_length=200, unique=True)
    slug = models.SlugField(max_length=10, unique=True, validators=[MinLengthValidator(5)])

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Ad(models.Model):
    """
    Клаcс-модели объявление
    """
    name = models.CharField(max_length=300, null=False, blank=False, validators=[MinLengthValidator(10)])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=500, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True, upload_to="ad_images")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name


class Selection(models.Model):
    """
    Клаcс-модели подборка-объявлений
    """
    name = models.CharField(max_length=300)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Ad)

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"

    def __str__(self):
        return self.name
