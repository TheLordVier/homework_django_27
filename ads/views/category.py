from rest_framework.viewsets import ModelViewSet

from ads.models import Category
from ads.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    """
    Представление (view) для работы с категориями
    """
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer
