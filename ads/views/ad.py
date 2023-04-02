from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from ads.models import Ad
from ads.permissions import IsStaff, IsOwner
from ads.serializers import AdSerializer, AdListSerializer, AdDetailSerializer


class AdViewSet(ModelViewSet):
    """
    Представление (view) для работы с объявлениями
    """
    queryset = Ad.objects.order_by("-price")
    default_serializer_class = AdSerializer

    default_permission = [AllowAny]
    permissions = {
        "retrieve": [IsAuthenticated],
        "update": [IsAuthenticated, IsStaff | IsOwner],
        "partial_update": [IsAuthenticated, IsStaff | IsOwner],
        "destroy": [IsAuthenticated, IsStaff | IsOwner],
    }

    serializers = {
        "list": AdListSerializer,
        "create": AdListSerializer,
        "retrieve": AdDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer_class)

    def get_permissions(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]

    def list(self, request, *args, **kwargs):
        categories = request.GET.getlist("cat")
        if categories:
            self.queryset = self.queryset.filter(category_id__in=categories)

        text = request.GET.get("text")
        if text:
            self.queryset = self.queryset.filter(name__icontains=text)

        location = request.GET.get("location")
        if location:
            self.queryset = self.queryset.filter(author__location__name__icontains=location)

        price_from = request.GET.get("price_from")
        if price_from:
            self.queryset = self.queryset.filter(price__gte=price_from)

        price_to = request.GET.get("price_to")
        if price_to:
            self.queryset = self.queryset.filter(price__lte=price_to)

        return super().list(request, *args, **kwargs)
