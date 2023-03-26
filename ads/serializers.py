from rest_framework import serializers

from ads.models import Ad, Category
from users.models import User
from users.serializers import UserDetailSerializer


class AdSerializer(serializers.ModelSerializer):
    """
    Клаcс-сериализатор объявления
    """

    class Meta:
        model = Ad
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """
    Клаcс-сериализатор категории
    """

    class Meta:
        model = Category
        fields = "__all__"


class AdListSerializer(serializers.ModelSerializer):
    """
    Клаcс-сериализатор списка объявлений
    """
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field="username"
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = Ad
        fields = "__all__"


class AdDetailSerializer(serializers.ModelSerializer):
    """
    Клаcс-сериализатор конкретного объявления
    """
    author = UserDetailSerializer()
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = Ad
        fields = "__all__"
