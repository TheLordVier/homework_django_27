from rest_framework.viewsets import ModelViewSet

from users.models import Location
from users.serializers import LocationSerializer


class LocationViewSet(ModelViewSet):
    """
    Представление (view) для работы с местонахождениями
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
