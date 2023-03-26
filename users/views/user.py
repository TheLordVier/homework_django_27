from django.db.models import Count, Q
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.pagination import PageNumberPagination

from users.models import User
from users.serializers import UserSerializer, UserListSerializer, UserCreateSerializer, UserUpdateSerializer


class UserPagination(PageNumberPagination):
    """
    Класс пагинации для пользователей
    """
    page_size = 6


class UserListView(ListAPIView):
    """
    Представление (view) для обращения ко всем пользователям
    """
    queryset = User.objects.annotate(total_ads=Count("ad", filter=Q(ad__is_published=True))).order_by("username")
    serializer_class = UserListSerializer
    pagination_class = UserPagination


class UserDetailView(RetrieveAPIView):
    """
    Представление (view) для обращения к конкретному пользователю по id
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateView(CreateAPIView):
    """
    Представление (view) для создания пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    """
    Представление (view) для обновления пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserDeleteView(DestroyAPIView):
    """
    Представление (view) для удаления пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
