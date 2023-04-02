from rest_framework import serializers
from rest_framework.fields import IntegerField

from users.models import User, Location


class UserSerializer(serializers.ModelSerializer):
    """
    Клаcс-сериализатор пользователя
    """

    class Meta:
        model = User
        exclude = ["password"]


class LocationSerializer(serializers.ModelSerializer):
    """
    Клаcс-сериализатор местонахождения
    """

    class Meta:
        model = Location
        fields = "__all__"


class UserListSerializer(serializers.ModelSerializer):
    """
    Клаcс-сериализатор списка пользователей
    """
    total_ads = IntegerField()

    class Meta:
        model = User
        exclude = ["password"]


class UserDetailSerializer(serializers.ModelSerializer):
    """
    Клаcс-сериализатор конкретного пользователя
    """
    location = LocationSerializer(many=True)

    class Meta:
        model = User
        exclude = ["password"]


class UserCreateSerializer(serializers.ModelSerializer):
    """
     Клаcс-сериализатор для создания пользователя
     """
    location = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = User
        fields = "__all__"

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.pop("location", [])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        password = validated_data.pop("password")
        new_user = User.objects.create(**validated_data)
        new_user.set_password(password)
        new_user.save()

        for location_name in self._locations:
            location, _ = Location.objects.get_or_create(name=location_name)
            new_user.location.add(location)

        new_user.save()
        return new_user


class UserUpdateSerializer(serializers.ModelSerializer):
    """
     Клаcс-сериализатор для обновления пользователя
     """
    location = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = User
        fields = "__all__"

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.pop("location", [])
        return super().is_valid(raise_exception=raise_exception)

    def save(self, **kwargs):
        user = super().save(**kwargs)
        user.location.clear()

        for location_name in self._locations:
            location, _ = Location.objects.get_or_create(name=location_name)
            user.location.add(location)

        user.save()
        return user
