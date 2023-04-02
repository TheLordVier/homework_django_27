from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from ads.models import Ad, Category, Selection
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


class SelectionSerializer(serializers.ModelSerializer):
    """
    Клаcс-сериализатор подборка-объявлений
    """

    class Meta:
        model = Selection
        fields = "__all__"


class SelectionDetailSerializer(serializers.ModelSerializer):
    """
    Клаcс-сериализатор конкретной подборки-объявлений
    """
    items = AdSerializer(many=True)

    class Meta:
        model = Selection
        fields = "__all__"


class SelectionListSerializer(serializers.ModelSerializer):
    """
    Клаcс-сериализатор списка подборки-объявлений
    """
    owner = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field="username"
    )

    class Meta:
        model = Selection
        fields = ["name", "owner"]


class SelectionCreateSerializer(serializers.ModelSerializer):
    """
    Клаcс-сериализатор создания подборки-объявлений
    """
    owner = SlugRelatedField(
        slug_field="username",
        read_only=True
    )

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["owner"] = request.user
        return super().create(validated_data)

    class Meta:
        model = Selection
        fields = "__all__"
