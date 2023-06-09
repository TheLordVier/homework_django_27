import factory.django

from ads.models import Category, Ad
from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    """
    Фабрика для модели User
    """
    class Meta:
        model = User

    username = factory.Faker("name")
    password = factory.Faker("password")


class CategoryFactory(factory.django.DjangoModelFactory):
    """
    Фабрика для модели Category
    """
    class Meta:
        model = Category

    name = factory.Faker("name")
    slug = factory.Faker("ean", length=8)


class AdFactory(factory.django.DjangoModelFactory):
    """
    Фабрика для модели Ad
    """
    class Meta:
        model = Ad

    name = factory.Faker("name")
    price = 100
    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(UserFactory)
